from abc import abstractmethod
from typing import Any, List

from fip11.models import Cluster
from confluent_kafka.admin import AdminClient, NewTopic, ConfigResource


class BaseClustersMetadata:
    def __init__(self):
        self.clusters = []

    async def initilize(self):
        self.clusters = await self.get_clusters()
        # connect to cluster here

    @abstractmethod
    async def get_clusters(self) -> List[Cluster]:
        pass

    def get_metadata(self) -> List[str]:
        if not self.clusters:
            raise ValueError(
                "There are no clusters initlized, please call initilize() first or check your configuration"
            )

        for cluster in self.clusters:
            admin_client = AdminClient(cluster.config)
