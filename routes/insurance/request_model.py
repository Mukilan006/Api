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


class EnrollRenewalRequest(CustomBaseModel):
    customer_id: int
    vehicle_name: str
    vehicle_no: str
    insurance_expiry_date: str
    fc_expiry_date: str
    premit_expiry_date: str
    pollution_expiry_date: str


class EnrollAccidentRequest(CustomBaseModel):
    customer_id: int
    company_name: str
    vehicle_no: str
    vehicle_name: str
    vehicle_regn_name: str
    customer_mobile: str
    driver_name: str
    driver_mobile: str
    insurance_name: str
    fir_status: str
    surveyoyar_name: str
    surveyoyar_mobile: str
    quotation_amount: str
    bill_amount: str
    claim_amount: str
