from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ProcessConf(BaseModel):
    plugins: Optional[List[str]] = Field(default=None)
    lmdb_map_size: Optional[str] = Field(default=None)
    router_flavor: Optional[str] = Field(default=None)
    cluster_max_payload: Optional[int] = Field(default=None)


class ConnectionState(BaseModel):
    is_connected: Optional[bool] = Field(default=None)


class Labels(BaseModel):
    region: Optional[str] = Field(default=None)
    provider: Optional[str] = Field(default=None)
    managed_by: Optional[str] = Field(default=None, alias="managed-by")
    network_id: Optional[str] = Field(default=None, alias="network-id")
    dp_group_id: Optional[str] = Field(default=None, alias="dp-group-id")


class Entity(BaseModel):
    type: Optional[str] = Field(default=None)
    id: Optional[str] = Field(default=None)
    host: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    path: Optional[str] = Field(default=None)
    port: Optional[int] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None)
    enabled: Optional[bool] = Field(default=None)
    retries: Optional[int] = Field(default=None)
    protocol: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    read_timeout: Optional[int] = Field(default=None)
    write_timeout: Optional[int] = Field(default=None)
    connect_timeout: Optional[int] = Field(default=None)
    methods: Optional[List[str]] = Field(default=None)
    paths: Optional[List[str]] = Field(default=None)
    hosts: Optional[List[str]] = Field(default=None)
    service_id: Optional[str] = Field(default=None)
    version: Optional[str] = Field(default=None)
    hostname: Optional[str] = Field(default=None)
    last_ping: Optional[datetime] = Field(default=None)
    config_hash: Optional[str] = Field(default=None)
    process_conf: Optional[ProcessConf] = Field(default=None)
    connection_state: Optional[ConnectionState] = Field(default=None)
    data_plane_cert_id: Optional[str] = Field(default=None)
    labels: Optional[Labels] = Field(default=None)
