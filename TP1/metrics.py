class Metrics:
    def __init__(self, param, success, depth, nodes_expanded, frontier, time):
        self.param = param
        self.success = success
        self.depth = depth
        self.nodes_expanded = nodes_expanded
        self.frontier = frontier
        self.time = time