import json
from routes.staff.model import *
from utility.utility import execute_stored_procedure


async def Dashboard(id=None):
    try:
        user = await execute_stored_procedure(
            proc_name="get_staff_details", params=[id]
        )
        user_details = {
            "user_details": user[0][0],
            "insurance_count": user[1][0].get("insurance_count"),
        }
        return user_details
    except Exception as error:
        raise Exception(str(error.args))


async def StaffList(pageNo=None, pageSize=None):
    try:
        result = await execute_stored_procedure(
            proc_name="get_staff_list", params=[pageNo, pageSize]
        )
        outResult = StaffListModel(
            total_records=result[0][0].get("total_record"),
            current_page=pageNo,
            staff_list=result[1],
        )
        return outResult.to_json()
    except Exception as error:
        raise Exception(str(error.args))


async def CustomerList(fromDate=None, toDate=None, pageNo=None, pageSize=None):
    try:
        result = await execute_stored_procedure(
            proc_name="get_customer_list", params=[pageNo, pageSize, fromDate, toDate]
        )
        outResult = CustomerListModel(
            total_records=result[0][0].get("total_record"),
            current_page=pageNo,
            customer_list=[
                CustomerDetailsModel(
                    id=item["id"],
                    first_name=item["first_name"],
                    mobile=item["mobile"],
                    gender=item["gender"],
                    created_date=item["created_date"],
                    enrolled_insurances=json.loads(item["enrolled_insurances"]),
                    enrolled_date=item["enrolled_date"],
                    status=item["status"],
                )
                for item in result[1]
            ],
        )
        return outResult.to_json()
    except Exception as error:
        raise Exception(str(error.args))


async def CustomerRegister(
    firstName=None, lastName=None, mobile=None, gender=None, staffId=None
):
    try:
        result = await execute_stored_procedure(
            proc_name="customer_register",
            params=[firstName, lastName, mobile, gender, staffId],
            is_one=True,
        )
        print(result)
        # outResult = {"customer_id": result.get("customer_id")}
        return "outResult"
    except Exception as error:
        raise Exception(str(error.args))


async def CustomerDetails(customerId: str = None):
    try:
        result = await execute_stored_procedure(
            "customer_details", [customerId], is_one=True
        )
        outResult = {"insurance_data": json.loads(result["insurance_data"])}
        return outResult
    except Exception as error:
        raise Exception(str(error.args))
