class Metrics:
    def __init__(self, param):
        self.param = param
        self.success = False
        self.depth = 0
        self.nodes_expanded = 0
        self.frontier = 0
        self.time = 0
        self.goal = None