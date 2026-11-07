"""Browser and JSON account routes sharing the prepared security services."""

from urllib.parse import parse_qsl

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, PublicUser, SignupInput

router = APIRouter()


def api_csrf_guard(request: Request):
    """Require session-bound CSRF for every API mutation."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Issue CSRF state without exposing authentication credentials."""
    return {"csrf_token": security.csrf_token(request, response)}


@router.post(
    "/api/signup",
    status_code=201,
    response_model=PublicUser,
    dependencies=[Depends(api_csrf_guard)],
)
def api_signup(request: Request, credentials: SignupInput):
    """Create only a member through the shared signup service."""
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings, credentials.username, credentials.password
    )


@router.post(
    "/api/login", response_model=PublicUser, dependencies=[Depends(api_csrf_guard)]
)
def api_login(request: Request, response: Response, credentials: LoginInput):
    """Set a protected cookie; return only public account fields."""
    return security.login(request, response, credentials.username, credentials.password)


@router.get("/api/me", response_model=PublicUser)
def api_me(user: dict = Depends(security.require_user)):
    """Reject private identity requests without a live session."""
    return {key: user[key] for key in ("id", "username", "role")}


@router.post("/api/logout", dependencies=[Depends(api_csrf_guard)])
def api_logout(request: Request, response: Response):
    """Revoke the server session as well as clearing its cookie."""
    security.logout(request, response)
    return {"message": "Logged out."}


def account_page(request, mode, error=None, username="", status_code=200):
    """Render with a fresh token while never retaining a password."""
    cookie_response = Response()
    token = security.csrf_token(request, cookie_response)
    response = request.app.state.templates.TemplateResponse(
        request=request,
        name="account.html",
        context={
            "mode": mode,
            "error": error,
            "username": username,
            "csrf_token": token,
        },
        status_code=status_code,
    )
    for key, value in cookie_response.raw_headers:
        if key == b"set-cookie":
            response.raw_headers.append((key, value))
    return response


async def form_values(request):
    """Bound form data and reject duplicate or unexpected fields."""
    if request.headers.get("content-type", "").split(";")[0] != (
        "application/x-www-form-urlencoded"
    ):
        raise HTTPException(415, "Please use the form on this page.")
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > 8192:
            raise HTTPException(413, "The submitted form is too large.")
    try:
        pairs = parse_qsl(
            body.decode("utf-8"),
            keep_blank_values=True,
            max_num_fields=4,
            errors="strict",
        )
    except (ValueError, UnicodeError) as error:
        raise HTTPException(422, "Please check the form fields.") from error
    values = dict(pairs)
    if len(values) != len(pairs):
        raise HTTPException(422, "Please submit each field only once.")
    security.require_csrf(request, values.pop("csrf_token", None))
    return values


@router.get("/signup", include_in_schema=False)
def signup_page(request: Request):
    """Show the member signup form."""
    return account_page(request, "signup")


@router.get("/login", include_in_schema=False)
def login_page(request: Request):
    """Show a login form without claiming authentication."""
    return account_page(request, "login")


async def submit_account(request, mode):
    """Validate both form types and call the same services as JSON routes."""
    username = ""
    try:
        values = await form_values(request)
        schema = SignupInput if mode == "signup" else LoginInput
        credentials = schema.model_validate(values)
        username = credentials.username
        if mode == "signup":
            security.limit_signup(request)
            security.signup(request.app.state.settings, username, credentials.password)
            return RedirectResponse("/login", status_code=303)
        response = RedirectResponse("/dashboard", status_code=303)
        security.login(request, response, username, credentials.password)
        return response
    except ValidationError:
        return account_page(
            request,
            mode,
            "Check your username and password requirements.",
            status_code=422,
        )
    except HTTPException as error:
        response = account_page(
            request, mode, error.detail, username, error.status_code
        )
        if error.headers:
            response.headers.update(error.headers)
        return response


@router.post("/signup", include_in_schema=False)
async def signup_form(request: Request):
    """Create an account from validated HTML fields."""
    return await submit_account(request, "signup")


@router.post("/login", include_in_schema=False)
async def login_form(request: Request):
    """Authenticate from validated HTML fields."""
    return await submit_account(request, "login")


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    """Check the live session before rendering private content."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    cookie_response = Response()
    token = security.csrf_token(request, cookie_response)
    return request.app.state.templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"user": user, "csrf_token": token},
    )


@router.post("/logout", include_in_schema=False)
async def logout_form(request: Request):
    """Require CSRF before ending the session and returning to login."""
    values = await form_values(request)
    if values:
        raise HTTPException(422, "Unexpected logout fields.")
    response = RedirectResponse("/login", status_code=303)
    security.logout(request, response)
    return response
