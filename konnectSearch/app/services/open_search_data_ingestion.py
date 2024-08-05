import logging

from app.db.entity_schema import Entity
from app.db.open_search import OpenSearchDBClient


class OpenSearchDataIngestion:
    _log = logging.getLogger(__name__)

    @classmethod
    async def ingest(cls, event):
        try:
            parsed_event = await cls._parse_event(event)
            os_client = OpenSearchDBClient.get_open_search_client()
            os_client.index(index=parsed_event["_index"], id=parsed_event["_id"], body=parsed_event["_source"])
            cls._log.info("Data Ingested Successfully {id}".format(id=parsed_event["_id"]))

        except Exception as e:
            cls._log.error("Exception While Ingesting Events")

    @classmethod
    async def _parse_event(cls, event):
        if event["after"]:
            key = event["after"]["key"]
            value = event["after"]["value"]["object"]
            doc_type = None
            if "/service/" in key:
                doc_type = "service"
            elif "/route/" in key:
                doc_type = "route"
            elif "/node/" in key:
                doc_type = "node"
            else:
                doc_type = "custom"
            value["type"] = doc_type
            entity = Entity(**value)
            data = {
                "_index": "entities",
                "_id": entity.id,
                "_source": entity.dict(by_alias=True)
            }
            return data


