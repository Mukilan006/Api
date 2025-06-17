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
