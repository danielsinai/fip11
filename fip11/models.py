from ast import List
from typing import Optional
from pydantic import BaseModel


class SaslOptions(BaseModel):
    username: str
    password: str
    mechanism: Optional[str]
    protocol: Optional[str]


class Cluster(BaseModel):
    name: str
    brokers: List[str]
    sasl: Optional[SaslOptions]
