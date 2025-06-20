from fastapi import APIRouter, Depends
from routes.staff.request_model import (
    CustomerListRequest,
    CustomerRegisterRequest,
    StaffListRequest,
    StaffUpdateRequest,
)
from routes.staff.services import *
from utility.custom_response import CustomResponse
from utility.utility import token_validator


staff = APIRouter()


@staff.get("/dashboard")
async def dashboard(user=Depends(token_validator)):
    try:
        userId = user.get("id")
        result = await Dashboard(id=userId)
        return CustomResponse(
            status=True, code=200, message="Dashboard Data Arrived", data=result
        )
    except Exception as error:
        return CustomResponse(code=400, status=False, message=str(error))


@staff.post("/staff_list")
async def staff_list(request: StaffListRequest, user=Depends(token_validator)):
    try:
        result = await StaffList(
            pageNo=request.page,
            pageSize=request.page_size,
        )
        return CustomResponse(
            status=True, code=200, message="Staff List Arrived", data=result
        )
    except Exception as error:
        return CustomResponse(code=400, status=False, message=str(error))


@staff.post("/customer_list")
async def customer_list(request: CustomerListRequest, user=Depends(token_validator)):
    try:
        result = await CustomerList(
            fromDate=request.from_date,
            toDate=request.to_date,
            pageNo=request.page,
            pageSize=request.page_size,
        )
        return CustomResponse(
            status=True, code=200, message="Customer List Arrived", data=result
        )
    except Exception as error:
        return CustomResponse(code=400, status=False, message=str(error))


@staff.post("/customer_register")
async def customer_register(
    request: CustomerRegisterRequest, user=Depends(token_validator)
):
    try:
        result = await CustomerRegister(
            firstName=request.first_name,
            lastName=request.last_name,
            mobile=request.mobile,
            gender=request.gender,
            staffId=user.get("id"),
        )
        return CustomResponse(
            status=True,
            code=200,
            message="Customer Register Successfully..!",
            data=result,
        )
    except Exception as error:
        return CustomResponse(code=400, status=False, message=str(error))
    
@staff.get("/customer_details/{customer_id}")
async def customer_details(customer_id=str,user=Depends(token_validator)):
    try:
        result = await CustomerDetails(customerId=customer_id)
        return CustomResponse(
            status=True,
            code=200,
            message="Customer Insurance Data Arrived Successfully..!",
            data=result,
        )
    except Exception as error:
        return CustomResponse(code=400, status=False, message=str(error))
# Customer Search
CustomerSearch
@staff.get("/customer_search/{customer_letter}")
async def customer_search(customer_letter=str,user=Depends(token_validator)):
    try:
        result = await CustomerSearch(letter=customer_letter)
        return CustomResponse(
            status=True,
            code=200,
            message="Customer Insurance Data Arrived Successfully..!",
            data=result,
        )
    except Exception as error:
        return CustomResponse(code=400, status=False, message=str(error))
    
@staff.post("/status_update")
async def status_update(
    request: StaffUpdateRequest, user=Depends(token_validator)
):
    try:
        result = await StatusUpdate(data=request)
        return CustomResponse(
            status=True,
            code=200,
            message=result,
            data={},
        )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))
