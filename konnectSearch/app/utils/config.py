import asyncio

from app.exceptions.exceptions import JsonDecodeException
from app.utils.json_utils import JsonUtils


class Config:
    _CONFIG = None
    _loop = asyncio.get_event_loop()

    @classmethod
    def load_config(cls, file_path):
        if cls._CONFIG is None:
            cls._CONFIG = JsonUtils.json_file_to_dict(file_path)

    @classmethod
    def get_config(cls, key: str = None):
        if cls._CONFIG is None:
            cls._CONFIG = JsonUtils.json_file_to_dict("./config.json")
        if cls._CONFIG is not None:
            if not key:
                return cls._CONFIG
            else:
                return cls._CONFIG.get(key)

    @classmethod
    def get_event_loop(cls):
        return cls._loop

