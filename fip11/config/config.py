import yaml
from typing import List, Literal, Optional
from pydantic import BaseModel

from fip11.models import SaslOptions


class StaticCluster(BaseModel):
    impl: Literal["static"]
    clsuter: 

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