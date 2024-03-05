import yaml
from typing import List, Literal, Optional
from pydantic import BaseModel, StrictStr


class SaslOptions(BaseModel):
    username: StrictStr
    password: StrictStr
    mechanism: Optional[StrictStr]
    protocol: Optional[StrictStr]

class StaticCluster(BaseModel):
    impl: Literal["static"]
    name: str
    brokers: List[str]
    sasl: Optional[SaslOptions]

class HTTPClsuters(BaseModel):
    impl: Literal["http"]
    url: str
    jqManipulation: str

class Config(BaseModel):
    clusters: List[StaticCluster] | HTTPClsuters

def read_yaml(file_path: str) -> dict:
    with open(file_path, 'r') as stream:
        config = yaml.safe_load(stream)
    
    return Config(**config).dict()

config = read_yaml('config.yaml')