from utility.utility import CustomBaseModel


class LoginRequest(CustomBaseModel):
    mobile: str
    password: str
    player_id: str


class RefreshTokenRequest(CustomBaseModel):
    refresh_token: str


class StaffRegisterRequest(CustomBaseModel):
    first_name: str
    last_name: str
    mobile: str
    role: str
    gender: str
    password: str

class LogoutRequest(CustomBaseModel):
    player_id : str
    
