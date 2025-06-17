from fastapi import APIRouter, Depends
from routes.common.request_model import (
    LoginRequest,
    LogoutRequest,
    RefreshTokenRequest,
    StaffRegisterRequest,
)
from routes.common.services import *
from utility.custom_response import CustomResponse
from utility.utility import *


common = APIRouter()


@common.post("/login")
async def login(data: LoginRequest):
    try:
        checkResult = execute_query(
            query="select user_check(%s,%s)",
            params=[data.mobile, data.password],
        )
        if checkResult == 1:
            result = await Login(
                mobile=data.mobile,
                pwd=data.password,
                playerId=data.player_id,
            )
            return CustomResponse(
                status=True,
                code=200,
                message="User logined successfully..!",
                data=result,
            )
        else:
            return CustomResponse(
                status=False, code=400, message="Invalid mobile or password"
            )
    except Exception as error:
        return CustomResponse(status=False, code=400, message=str(error))


@common.post("/refresh_token")
async def refresh_token(data: RefreshTokenRequest):
    try:
        result = await RefreshToken(refreshToken=data.refresh_token)
        return CustomResponse(
            status=True,
            code=200,
            message="User relogined successfully..!",
            data=result,
        )
    except Exception as error:
        return CustomResponse(status=False, message=str(error), code=400)


@common.post("/staff_register")
async def staff_register(request: StaffRegisterRequest):
    try:
        result = await StaffRegister(data=request)
        return CustomResponse(
            status=True,
            code=200,
            message="staff registered successfully..!",
            data=result,
        )
    except Exception as error:
        return CustomResponse(status=False, message=str(error), code=400)


@common.post("/logout")
async def logout(request: LogoutRequest, user=Depends(token_validator)):
    try:
        result = await Logout(data=request,userId=user.get("id"))
        return CustomResponse(
            status=True,
            code=200,
            message="logged out successfully..!",
            data=result,
        )
    except Exception as error:
        return CustomResponse(status=False, message=str(error), code=400)
