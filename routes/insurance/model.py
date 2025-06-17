from datetime import date, datetime
from typing import Dict, List


class InsuranceListModel:
    total_records: int
    current_page: int
    insurance_list: list

    def __init__(
        self, total_records: int, current_page: int, insurance_list: list
    ) -> None:
        self.total_records = total_records
        self.current_page = current_page
        self.insurance_list = insurance_list

    def to_json(self) -> dict:
        return {
            "total_records": self.total_records,
            "current_page": self.current_page,
            "insurance_list": self.insurance_list,
        }
    
class DynamicRecord:
    def __init__(self, data: Dict[str, any]) -> None:
        self.data = data

    def to_json(self) -> Dict[str, any]:
        # Convert datetime or date objects to ISO strings
        return {
            k: (v.strftime('%Y-%m-%d') if isinstance(v, (datetime, date)) else v)
            for k, v in self.data.items()
        }

    @staticmethod
    def get_unique_fields(record_list: List[Dict[str, any]]) -> List[str]:
        field_set = set()
        for record in record_list:
            field_set.update(record.keys())
        return list(field_set)

    

class Customdata:
    def __init__(self, table_data: List[Dict[str, any]] = None) -> None:
        self.records = [DynamicRecord(row) for row in (table_data or [])]

    def to_json(self) -> List[Dict[str, any]]:
        return [record.to_json() for record in self.records]

    def to_fields(self) -> List[str]:
        return DynamicRecord.get_unique_fields(self.to_json())
