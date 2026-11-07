"""Read-only administration routes guarded by current server-side permissions."""

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from app.security import require_admin

router = APIRouter()


@router.get("/api/admin", dependencies=[Depends(require_admin)])
def admin_status():
    """Expose the administration status only to current administrators."""
    return {"message": "Administrator access confirmed."}


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request):
    """Use the API's permission check and present a browser-friendly response."""
    try:
        require_admin(request)
    except HTTPException as error:
        if error.status_code == 401:
            return RedirectResponse("/login", status_code=303)
        if error.status_code != 403:
            raise
        return request.app.state.templates.TemplateResponse(
            request=request, name="admin_denied.html", status_code=403
        )
    return request.app.state.templates.TemplateResponse(
        request=request, name="admin.html"
    )
