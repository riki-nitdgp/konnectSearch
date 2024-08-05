import logging

from app.utils.config import Config


class BaseConsumer:
    _config = Config.get_config("KAFKA")
    _event_loop = Config.get_event_loop()
    _log = logging.getLogger(__name__)
    _consumer = None

    @classmethod
    async def initialize_consumer(cls):
        pass

    @classmethod
    async def consume(cls):
        pass

    @classmethod
    async def stop(cls):
        pass