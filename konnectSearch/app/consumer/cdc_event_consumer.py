from aiokafka import AIOKafkaConsumer
from app.consumer.base_consumer import BaseConsumer
from app.services.open_search_data_ingestion import OpenSearchDataIngestion
from app.utils.config import Config
import json


class CDCEventConsumer(BaseConsumer):

    @classmethod
    async def initialize_consumer(cls):
        if cls._consumer is None:
            config = Config.get_config("KAFKA")
            cls._consumer = AIOKafkaConsumer(
                config.get("TOPICS", {}).get("CDC_EVENT"),
                bootstrap_servers=config.get("BOOTSTRAP_SERVER"),
                group_id=config.get("GROUP_ID")
            )
            await cls._consumer.start()

    @classmethod
    async def consume(cls):
        await cls.initialize_consumer()
        try:
            async for msg in cls._consumer:
                cls._log.info(f"Consumed message: {msg.value} from topic: {msg.topic}")
                await OpenSearchDataIngestion.ingest(json.loads(msg.value))
        except Exception as e:
            cls._log.error(f"Error consuming messages: {str(e)}")
        finally:
            await cls._consumer.stop()

    @classmethod
    async def stop(cls):
        await cls._consumer.stop()
