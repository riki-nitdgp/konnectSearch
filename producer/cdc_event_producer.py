import asyncio
import json

from aiokafka import AIOKafkaProducer


class CDCEventProducer:
    _topic = "cdc-events"
    _producer = None
    _kafka_config = {
        'bootstrap_servers': '0.0.0.0:9092',
        'compression_type': 'snappy',
        'acks': 'all',
    }

    @classmethod
    async def initialize_producer(cls):
        cls._producer = AIOKafkaProducer(**cls._kafka_config)
        await cls._producer.start()
        print("Kafka producer initialized")

    @classmethod
    async def produce(cls, message):
        if cls._producer is None:
            raise Exception("Producer not initialized. Call 'initialize_producer' first.")
        key = message.get("after", {}).get("key", "default").encode('utf-8')
        value = json.dumps(message).encode('utf-8')
        try:
            await cls._producer.send_and_wait(cls._topic, key=key, value=value)
            print(f'Message delivered to {cls._topic}')
        except Exception as e:
            print(f'Failed to deliver message: {e}')

    @classmethod
    def parse_events(cls):
        file_path = './stream.jsonl'
        with open(file_path, 'r') as file:
            lines = file.readlines()
        events = [json.loads(line) for line in lines]
        return events

    @classmethod
    async def parse_and_produce(cls):
        parse_events = cls.parse_events()
        for event in parse_events:
            await cls.produce(event)

    @classmethod
    async def close_producer(cls):
        if cls._producer:
            await cls._producer.stop()
            print("Kafka producer closed")


async def main():
    await CDCEventProducer.initialize_producer()
    await CDCEventProducer.parse_and_produce()
    await CDCEventProducer.close_producer()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())