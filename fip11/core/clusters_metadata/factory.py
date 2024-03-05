class Factory:
    def __init__(self, config, cluster, **kwargs):
        self.config = config
        self.cluster = cluster
        self.kwargs = kwargs

    def create(self):
        return self.cluster(self.config, **self.kwargs)

    def __call__(self):
        return self.create()