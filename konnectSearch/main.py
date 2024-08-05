import asyncio

import uvicorn
from fastapi import FastAPI

from app.consumer.cdc_event_consumer import CDCEventConsumer
from app.db.open_search import OpenSearchDBClient
from app.exceptions.error_handler import (
    application_error_handler,
    internal_server_error_handler,
    json_decoder_error_handler,
    debug_exception_handler
)

from app.exceptions.exceptions import ServiceException, InternalServiceException, JsonDecodeException
from app.utils.config import Config
from app.controller.routes import router as api_route
from app.utils.log_utils import LogUtils


def create_application() -> FastAPI:
    Config.load_config("./config.json")
    config = Config.get_config()
    application = FastAPI(title=config.get("SERVICE_NAME"), debug=config.get("DEBUG"))
    add_exception_handler(application)
    LogUtils.setup()
    application.include_router(api_route, prefix=config.get("API_PREFIX"))
    return application


def add_exception_handler(application: FastAPI):
    application.add_exception_handler(ServiceException, application_error_handler)
    application.add_exception_handler(InternalServiceException, internal_server_error_handler)
    application.add_exception_handler(JsonDecodeException, json_decoder_error_handler)
    application.add_exception_handler(Exception, debug_exception_handler)


app = create_application()


@app.on_event("startup")
async def start_up_event():
    await CDCEventConsumer.initialize_consumer()
    OpenSearchDBClient.init_open_search_client()
    OpenSearchDBClient.create_index_if_not_exist()
    # Start the consume task
    app.state = {}
    app.state["cdc_consumer_task"] = asyncio.create_task(CDCEventConsumer.consume())


@app.on_event("shutdown")
async def shutdown_event():
    app.state["cdc_consumer_task"].cancel()
    await CDCEventConsumer.stop()


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
