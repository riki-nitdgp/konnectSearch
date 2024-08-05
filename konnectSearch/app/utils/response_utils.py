from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class ResponseUtils:

    @classmethod
    def build_error_response(cls, message, status_code=400):
        response = {
            "error": [{"message": message}],
            "is_success": False,
            "status_code": status_code,
        }
        return JSONResponse(content=jsonable_encoder(response), status_code=status_code)

    @classmethod
    def build_success_response(cls, data: dict, status_code: int = 200, metadata: dict = {}):
        response = {
            "data": data,
            "status_code": status_code,
            "is_success": True,
            "meta": metadata
        }
        return JSONResponse(content=jsonable_encoder(response), headers={"Access-Control-Allow-Origin": "*"})