from utility.utility import CustomBaseModel


class StaffListRequest(CustomBaseModel):
    page: int
    page_size: int


class CustomerListRequest(CustomBaseModel):
    from_date: str
    to_date: str
    page: int
    page_size: int


class CustomerRegisterRequest(CustomBaseModel):
    first_name: str
    last_name: str
    mobile: str
    gender: str


class StaffUpdateRequest(CustomBaseModel):
    id: int
    status: bool


class StaffUpdateRequest(CustomBaseModel):
    first_name: str
    last_name: str
    gender: str
    password : str

class CustomerUpdateRequest(CustomBaseModel):
    first_name: str
    last_name: str
    gender: str
class ChangePasswordRequest(CustomBaseModel):
    old_password: str
    new_password: str
 
