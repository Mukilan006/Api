from routes.common.model import *
from routes.common.request_model import LogoutRequest, StaffRegisterRequest
from utility.utility import *


async def Login(mobile=None, pwd=None, playerId=None):
    try:
        users = await execute_stored_procedure(
            proc_name="user_login", params=[mobile, pwd, playerId], is_one=True
        )
        if users:
            user_details = UserDetails(
                id=users.get("id"),
                first_name=users.get("first_name"),
                status=users.get("status"),
            )
            result = await createTokens(user=user_details)
            return result
    except Exception as error:
        raise Exception(str(error)) from error


async def createTokens(user):
    try:
        ac_token = create_access_token(user=user)
        rf_token = create_refresh_token(user=user)
        result = LoginResponse(
            access_token=ac_token,
            refresh_token=rf_token,
            id=user.id,
            first_name=user.first_name,
            status=user.status,
        ).to_json()
        return result
    except Exception as error:
        raise Exception(str(error)) from error


async def RefreshToken(refreshToken=None):
    try:
        if refreshToken is not None:
            decoded = jwt.decode(
                refreshToken,
                settings.SECRET_KEY,
                algorithms="HS256",
                audience="wpf",
                options={
                    "require_iat": True,
                    "require_exp": True,
                },
                leeway=30,
            )
            if decoded["type"] == "refresh":
                users = await execute_stored_procedure(
                    "get_user", [decoded["id"]], is_one=True
                )

                user_details = UserDetails(
                    id=users.get("id"),
                    first_name=users.get("first_name"),
                    status=users.get("status"),
                )
                outresult = await createTokens(user=user_details)
                return outresult
            else:
                raise Exception("Invalid Refresh Token")

    except Exception as error:
        raise Exception(str(error)) from error


async def StaffRegister(data: StaffRegisterRequest = None):
    try:
        await execute_stored_procedure(
            proc_name="staff_registration",
            params=[
                data.first_name,
                data.last_name,
                data.mobile,
                data.password,
                data.role,
                data.gender,
            ],
            is_one=True,
        )
        return "User registerd successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error


async def Logout(data: LogoutRequest = None, userId=None):
    try:
        await execute_stored_procedure(
            proc_name="status_update",
            params=[userId, "logout", data.player_id, 0],
        )
        return "User logout successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error
