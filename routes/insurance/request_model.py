from typing import List
from utility.utility import CustomBaseModel


class InsuranceListRequest(CustomBaseModel):
    page: int
    page_size: int


class PdfDownloadRequest(CustomBaseModel):
    keys: str
    selected_values: List[str]


class EnrollHealthRequest(CustomBaseModel):
    customer_id: int
    company_name: str
    policy_number: str
    mobile: str
    amount: str
    from_date: str
    to_date: str
    idv: str


class EnrollLifeRequest(CustomBaseModel):
    customer_id: int
    company_name: str
    policy_number: str
    mobile: str
    amount: str
    from_date: str
    to_date: str
    idv: str


class EnrollFastagRequest(CustomBaseModel):
    customer_id: int
    fastag_name: str
    vehicle_no: str
    vehicle_name: str
    mobile: str
    bank_name: str


class EnrollFinanceRequest(CustomBaseModel):
    customer_id: int
    finance_name: str
    vehicle_no: str
    from_date: str
    to_date: str
    emi_amount: str


class EnrollMaintenanceRequest(CustomBaseModel):
    customer_id: int
    purpose: str
    vehicle_name: str
    vehicle_no: str
    date: str
    kilometer: str
