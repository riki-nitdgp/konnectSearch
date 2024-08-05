import logging

from app.utils.config import Config
from opensearchpy import OpenSearch
from app.utils.json_utils import JsonUtils

class OpenSearchDBClient:
    _open_search_client = None
    _config = Config.get_config("OPEN_SEARCH")
    _log = logging.getLogger(__name__)

    @classmethod
    def init_open_search_client(cls):
        if not cls._open_search_client:
            cls._open_search_client = OpenSearch(
                hosts=[{"host": cls._config.get("HOST")}],
                http_compress=True,
                use_ssl=False
            )
            cls._log.info("OpenSearch Connected Successfully")

    @classmethod
    def get_open_search_client(cls):
        if not cls._open_search_client:
            cls.init_open_search_client()
        return cls._open_search_client

    @classmethod
    def create_index_if_not_exist(cls):
        index_name = cls._config.get("INDEXES").get("ENTITIES")
        body = JsonUtils.json_file_to_dict("./schema.json")
        if not cls._open_search_client.indices.exists(index_name):
            cls._open_search_client.indices.create(index=index_name, body=body)


