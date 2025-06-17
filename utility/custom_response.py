from fastapi.responses import JSONResponse


def CustomResponse(code: int = None, status: bool = None, message=None, data=None):
    def error_dict_to_str(errors):
        if isinstance(errors, dict):
            key = next(iter(errors.keys()), "")
            value = next(iter(errors.values()), [""])
            if isinstance(value, list) and value:
                value = value[0]
            return f"{key}: {value}"
        return str(errors)

    response_data = {
        "response": "success" if status else "failure",
        "success": {
            "code": code if code == 200 else -1,
            "msg": message if code == 200 else "",
            "result": data if status else {},
        },
        "failure": {
            "code": -1 if code == 200 else code,
            "msg": error_dict_to_str(message) if code != 200 else "",
        },
    }

    return JSONResponse(content=response_data, status_code=401 if code == 401 else 200)
