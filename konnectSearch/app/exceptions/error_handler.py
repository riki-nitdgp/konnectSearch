import traceback

from fastapi import Request
from starlette.responses import JSONResponse
from starlette import status
from app.exceptions.exceptions import ServiceException, JsonDecodeException, InternalServiceException
from app.utils.response_utils import ResponseUtils


async def application_error_handler(_: Request, exc: ServiceException) -> JSONResponse:
    return ResponseUtils.build_error_response(exc.error, status_code=exc.status_code)


async def internal_server_error_handler(_: Request, exc: InternalServiceException) -> JSONResponse:
    return ResponseUtils.build_error_response(exc.error, status_code=exc.status_code)


async def debug_exception_handler(_: Request, exc: Exception):
    error = " ".join(traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__))
    _.app.logger.error(error)
    return ResponseUtils.build_error_response("Internal Server Error Occuerd",
                                              status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def json_decoder_error_handler(_: Request, exc: JsonDecodeException) -> JSONResponse:
    return ResponseUtils.build_error_response(exc.error, status_code=exc.status_code)
