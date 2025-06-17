from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from settings import Settings
from routes.common import common_controller
from routes.staff import staff_controller
from routes.insurance import insurance_controller
from utility.custom_response import CustomResponse

settings = Settings()

app = FastAPI(
    # debug=settings.DEBUG,
    # docs_url=None,
    # redoc_url= None,
    # title="Test Api",
    # openapi_url=None
)

app.include_router(router=common_controller.common, prefix="/common")
app.include_router(router=staff_controller.staff, prefix="/staff")
app.include_router(router=insurance_controller.insurance, prefix="/insurance")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_details = []
    for err in exc.errors():
        loc = str(err["loc"][-1])
        msg = err["msg"]
        error_details.append(f"{loc}:{msg}")

    return CustomResponse(
        code=400,
        status=False,
        message=error_details,
    )


@app.get("/")
def read_root():
    return "Api is working"
