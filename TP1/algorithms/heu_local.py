from metrics import Metrics
#from algorithms.search import get_depth
from logging import root
from metrics import Metrics
from solution import GOAL_STATE
from solution import possible_moves
from solution import next
from algorithms.search import Search
from time import perf_counter

class LocalHeuristic(Search):
    def __init__(self):
        super().__init__()
        self.heumethod = None
        self.metrics = Metrics('LOCAL_H')

    def setHeuristic(self, heu):
        self.heumethod = heu

    def search(self, root_node):
        L = [root_node]
        return self.local_heuristic_search(L)

    def local_heuristic_search(self, nodes):
        t1_start = perf_counter()
        metrics = self.metrics
        Ex = set()
        while nodes:
            node = nodes.pop(0)
            Ex.add(node)
            metrics.nodes_expanded +=1

            if node.__eq__(GOAL_STATE):
                print ("encontrado")
                metrics.success = True
                metrics.frontier = len(nodes)
                print(node.get_trace())
                t1_stop = perf_counter() 
                metrics.time = (t1_stop-t1_start)
                metrics.depth = node.depth
                return metrics
            
            moves = possible_moves(node.matrix, node.blankspace)
            for move in moves:
                nextNode = next(node.matrix, node.blankspace, move, node)
                if nextNode not in Ex:
                    nodes.append(nextNode)
            
            nodes.sort(key = self.heumethod)