from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services import ach, alerts, audit

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {
        "transfers": ach.list_transfers(),
        "alerts": alerts.list_alerts(),
        "audit_events": audit.list_events(),
    })


@router.post("/transfers", response_class=RedirectResponse)
async def submit_transfer(
    originator: str = Form(...),
    beneficiary: str = Form(...),
    amount: float = Form(...),
    routing_number: str = Form(...),
    account_number: str = Form(...),
    memo: str = Form(""),
):
    ach.submit_transfer(
        originator=originator,
        beneficiary=beneficiary,
        amount=amount,
        routing_number=routing_number,
        account_number=account_number,
        memo=memo,
    )
    return RedirectResponse(url="/", status_code=303)
