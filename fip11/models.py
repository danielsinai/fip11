from typing import Dict
from pydantic import BaseModel


class Cluster(BaseModel):
    name: str
    config: Dict[str, str]
