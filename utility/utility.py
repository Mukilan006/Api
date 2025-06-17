import datetime
from io import BytesIO
from fastapi import HTTPException, Request
import jwt
from pydantic import BaseModel, model_validator
from pymysql import DatabaseError
from settings import Settings
from database import get_connection
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.lib import colors


settings = Settings()


# Function to execute store procedure
async def execute_stored_procedure(proc_name, params=None, is_one=False):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.callproc(procname=proc_name, args=params or [])
            result = []
            while True:
                if is_one:
                    row = cursor.fetchone()
                    if row:
                        colums = [col[0] for col in cursor.description]
                        result.append(dict(zip(colums, row)))
                    else:
                        result.append([])
                else:
                    row = cursor.fetchall()
                    if row:
                        colums = [col[0] for col in cursor.description]
                        result_set = [dict(zip(colums, row)) for row in row]
                        result.append(result_set)
                    else:
                        if cursor.description:
                            result.append([])
                if not cursor.nextset():
                    break
                # print(result)
            return result[0] if is_one else result
    except DatabaseError as e:
        raise Exception(f"DB Error in `{proc_name}`: {str(e.args[1])}") from e
    except Exception as e:
        raise Exception(f"Unknown error in `{proc_name}`: {str(e)}") from e
    finally:
        conn.close()


# Function to execute query or function
def execute_query(query, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params or ())
            row = cursor.fetchone()
            return row[0] if row else None
    except DatabaseError as e:
        raise Exception(f"DB Error: {str(e.args[1])}") from e
    except Exception as e:
        raise Exception(f"Unknown errordd: {str(e)}") from e
    finally:
        conn.close()


# Function create access token and return token.
def create_access_token(user) -> str:
    try:
        payload = {
            "id": user.id,
            "first_name": user.first_name,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=1),  # Access token expiry
            "iat": datetime.datetime.utcnow(),
            "aud": "wpf",
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token
    except Exception as error:
        raise Exception(str(error)) from error


# Function create refresh token and return token.
def create_refresh_token(user) -> str:
    try:
        payload = {
            "id": user.id,
            "type": "refresh",
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=2),  # Refresh token expiry
            "iat": datetime.datetime.utcnow(),
            "aud": "wpf",
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token
    except Exception as error:
        raise Exception(str(error)) from error


# Function token validator and return user id.
def token_validator(request: Request):
    token = request.headers.get("Authorization")
    if token == None or token is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    try:
        if token.startswith("Bearer "):
            token_parts = token.split(" ")
            if len(token_parts) == 2:
                decoded = jwt.decode(
                    token_parts[1],
                    settings.SECRET_KEY,
                    algorithms=["HS256"],
                    audience="wpf",
                    options={
                        "require_iat": True,
                        "require_exp": True,
                    },
                    leeway=30,
                )

                id = decoded.get("id")
                result = execute_query("select user_check_id(%s)", [int(id)])
                if result == 1:
                    return {"id": id}
                else:
                    raise HTTPException(status_code=401, detail="Unauthorized token")

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


class CustomBaseModel(BaseModel):
    @model_validator(mode="after")
    def check_no_empty_values(cls, model):
        def validate(value: any, path: str = ""):
            if isinstance(value, str):
                if not value.strip():
                    raise ValueError(f"Field '{path}' contains an empty string.")
            elif isinstance(value, list):
                if not value:
                    raise ValueError(f"Field '{path}' contains an empty list.")
                for i, v in enumerate(value):
                    validate(v, f"{path}[{i}]")
            elif isinstance(value, dict):
                if not value:
                    raise ValueError(f"Field '{path}' contains an empty dict.")
                for k, v in value.items():
                    validate(v, f"{path}.{k}" if path else k)
            elif isinstance(value, BaseModel):
                for k, v in value.__dict__.items():
                    validate(v, f"{path}.{k}" if path else k)

        validate(model)
        return model


async def pdf_convert(datas=None, fields=None):
    try:
        buffer = BytesIO()
        # Set up the PDF document
        doc = SimpleDocTemplate(
            buffer,
            pagesize=landscape(A4) if len(fields) > 5 else portrait(A4),
            rightMargin=20,
            leftMargin=20,
            topMargin=20,
            bottomMargin=20,
        )
        elements = []
        # Use keys from first dict if fields not provided
        if not fields:
            fields = list(datas[0].keys())

        # Header row: formatted field names
        def format_fields(fields: list[str]) -> list[str]:
            return [field.replace("_", " ").title() for field in fields]

        data = [format_fields(fields)]  # Header row as a list of strings

        # Data rows
        for row in datas:
            data.append([row.get(field, "") for field in fields])
        table = Table(data, repeatRows=1)
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ]
            )
        )

        elements.append(table)
        doc.build(elements)
        buffer.seek(0)
        return buffer
    except Exception as e:
        raise Exception(str(e))
