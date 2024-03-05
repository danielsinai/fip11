from abc import abstractmethod
from typing import List

from fip11.models import Cluster


class BaseClusterListRetriever:
    def __init__(self, cluster_list: List[Cluster]):
        self.cluster_list = cluster_list

    @abstractmethod
    def retrieve(self) -> List[str]:
        return self.cluster_list
