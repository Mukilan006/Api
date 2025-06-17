from typing import List


class StaffListModel:
    total_records: int
    current_page: int
    staff_list: List

    def __init__(self, total_records: int, current_page: int, staff_list: List) -> None:
        self.total_records = total_records
        self.current_page = current_page
        self.staff_list = staff_list

    def to_json(self) -> dict:
        return {
            "total_records": self.total_records,
            "current_page": self.current_page,
            "staff_list": self.staff_list,
        }


class CustomerDetailsModel:
    id: int
    first_name: str
    mobile: str
    gender: str
    created_date: str
    enrolled_insurances: List
    enrolled_date: str
    status: bool

    def __init__(
        self,
        id: int,
        first_name: str,
        mobile: str,
        gender: str,
        created_date: str,
        enrolled_insurances: List,
        enrolled_date: str,
        status: bool,
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.mobile = mobile
        self.gender = gender
        self.created_date = created_date
        self.enrolled_insurances = enrolled_insurances
        self.enrolled_date = enrolled_date
        self.status = status

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "mobile": self.mobile,
            "gender": self.gender,
            "created_date": self.created_date,
            "enrolled_insurances": self.enrolled_insurances,
            "enrolled_date": self.enrolled_date,
            "status": self.status,
        }


class CustomerListModel:
    total_records: int
    current_page: int
    customer_list: List[CustomerDetailsModel]

    def __init__(
        self,
        total_records: int,
        current_page: int,
        customer_list: List[CustomerDetailsModel],
    ) -> None:
        self.total_records = total_records
        self.current_page = current_page
        self.customer_list = customer_list

    def to_json(self) -> dict:
        return {
            "total_records": self.total_records,
            "current_page": self.current_page,
            "customer_list": [customer.to_json() for customer in self.customer_list],
        }
