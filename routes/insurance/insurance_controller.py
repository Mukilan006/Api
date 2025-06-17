from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from routes.insurance.request_model import (
    EnrollAccidentRequest,
    EnrollFinanceRequest,
    EnrollHealthRequest,
    EnrollLifeRequest,
    EnrollMaintenanceRequest,
    EnrollRenewalRequest,
    InsuranceListRequest,
    PdfDownloadRequest,
    EnrollFastagRequest,
)
from routes.insurance.services import *
from utility.custom_response import CustomResponse
from utility.utility import token_validator


insurance = APIRouter()


@insurance.post("/insurance_list")
async def insurance_list(request: InsuranceListRequest, user=Depends(token_validator)):
    try:
        result = await InsuranceList(page=request.page, pageSize=request.page_size)
        return CustomResponse(
            status=True,
            message="Data Arrived",
            code=200,
            data=result,
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.get("/get_insurance_title/{pare_key}")
async def get_insurance_title(pare_key: str, user=Depends(token_validator)):
    try:
        result = await GetInsuranceTitle(pareKey=pare_key)
        return CustomResponse(
            status=True, message="insurance title arrived", code=200, data=result
        )
    except Exception as e:
        return CustomResponse(status=False, message=str(e), code=400)


@insurance.post("/download_pdf")
async def download_pdf(req: PdfDownloadRequest):
    try:
        result = await DownloadPdf(pareKey=req.keys, fileds=req.selected_values)
        return StreamingResponse(
            result,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=report.pdf"},
        )
    except Exception as e:
        return CustomResponse(status=False, message=str(e), code=400)


@insurance.post("/enroll_health")
async def enroll_health(request: EnrollHealthRequest, user=Depends(token_validator)):
    try:
        result = await EnrollHealth(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.post("/enroll_life")
async def enroll_life(request: EnrollLifeRequest, user=Depends(token_validator)):
    try:
        result = await EnrollHealth(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.post("/enroll_fastag")
async def enroll_fastag(request: EnrollFastagRequest, user=Depends(token_validator)):
    try:
        result = await EnrollFastag(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.post("/enroll_finance")
async def enroll_finance(request: EnrollFinanceRequest, user=Depends(token_validator)):
    try:
        result = await EnrollFinance(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.post("/enroll_maintenance")
async def enroll_finance(
    request: EnrollMaintenanceRequest, user=Depends(token_validator)
):
    try:
        result = await EnrollMaintenance(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.post("/enroll_renewal")
async def enroll_renewal(request: EnrollRenewalRequest, user=Depends(token_validator)):
    try:
        result = await EnrollRenewal(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@insurance.post("/enroll_accident")
async def enroll_accident(
    request: EnrollAccidentRequest, user=Depends(token_validator)
):
    try:
        result = await EnrollAccident(data=request, staffId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))
