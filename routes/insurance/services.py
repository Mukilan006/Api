from routes.insurance.model import Customdata, InsuranceListModel
from routes.insurance.request_model import (
    EnrollFastagRequest,
    EnrollFinanceRequest,
    EnrollHealthRequest,
    EnrollLifeRequest,
    EnrollMaintenanceRequest,
)
from utility.utility import execute_stored_procedure, pdf_convert


async def InsuranceList(page=None, pageSize=None):
    try:
        result = await execute_stored_procedure(
            proc_name="get_insurance_list", params=[page, pageSize]
        )
        response = InsuranceListModel(
            total_records=result[0][0].get("total_record"),
            current_page=page,
            insurance_list=result[1],
        )
        return response.to_json()
    except Exception as error:
        raise Exception(str(error)) from error


async def GetInsuranceTitle(pareKey=None):
    try:
        result = await execute_stored_procedure(
            proc_name="get_insurance_title", params=[pareKey]
        )
        return {
            "title_list": (
                [] if result[0] == [] else [item["titles"] for item in result[0]]
            )
        }
    except Exception as error:
        raise Exception(str(error)) from error


async def DownloadPdf(pareKey=None, fileds=None):
    try:
        result = await execute_stored_procedure(
            proc_name="get_table_view", params=[pareKey]
        )
        user_data = Customdata(result[0])
        replace_map = {"staff_id": "staff_name", "customer_id": "customer_name"}
        updated_list = [replace_map.get(field, field) for field in fileds]
        fields = [field for field in user_data.to_fields() if field in updated_list]
        returnFile = await pdf_convert(datas=user_data.to_json(), fields=fields)
        return returnFile
    except Exception as error:
        raise Exception(str(error)) from error


async def EnrollHealth(data: EnrollHealthRequest = None, staffId=None):
    try:
        result = await execute_stored_procedure(
            proc_name="health_enroll",
            params=[
                data.customer_id,
                staffId,
                data.company_name,
                data.policy_number,
                data.mobile,
                data.amount,
                data.from_date,
                data.to_date,
                data.idv,
            ],
        )
        return "health insurance enroll successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error


async def EnrollLife(data: EnrollLifeRequest = None, staffId=None):
    try:
        result = await execute_stored_procedure(
            proc_name="life_enroll",
            params=[
                data.customer_id,
                staffId,
                data.company_name,
                data.policy_number,
                data.mobile,
                data.amount,
                data.from_date,
                data.to_date,
                data.idv,
            ],
        )
        return "health insurance enroll successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error


async def EnrollFastag(data: EnrollFastagRequest = None, staffId=None):
    try:
        result = await execute_stored_procedure(
            proc_name="fastag_enroll",
            params=[
                staffId,
                data.customer_id,
                data.fastag_name,
                data.vehicle_no,
                data.vehicle_name,
                data.mobile,
                data.bank_name,
            ],
        )
        return "Fastag enroll successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error


async def EnrollFinance(data: EnrollFinanceRequest = None, staffId=None):
    try:
        result = await execute_stored_procedure(
            proc_name="finacnce_enroll",
            params=[
                staffId,
                data.customer_id,
                data.finance_name,
                data.vehicle_no,
                data.from_date,
                data.to_date,
                data.emi_amount,
            ],
        )
        return "Finance enroll successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error


async def EnrollMaintenance(data: EnrollMaintenanceRequest = None, staffId=None):
    try:
        result = await execute_stored_procedure(
            proc_name="maintenance_enroll",
            params=[
                staffId,
                data.customer_id,
                data.purpose,
                data.vehicle_name,
                data.vehicle_no,
                data.date,
                data.kilometer,
            ],
        )
        return "Maintenance enroll successfully...!"
    except Exception as error:
        raise Exception(str(error)) from error
