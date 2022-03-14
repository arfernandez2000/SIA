from metrics import Metrics
#from algorithms.search import get_depth
from logging import root
from metrics import Metrics
from solution import GOAL_STATE
from solution import possible_moves
from solution import next
from algorithms.search import Search
from time import perf_counter

class AStar(Search):
    def __init__(self):
        super().__init__()
        self.heumethod = None
        self.metrics = Metrics('A_STAR')
    
    def setHeuristic(self, heu):
        self.heumethod = heu

    def f(self, node):
        return node.depth + self.heumethod(node)

    def search(self, root_node):
        t1_start = perf_counter()
        A = []
        F = []
        Ex = set()
        metrics = self.metrics
        F.append(root_node)
        A.append(root_node)

        while len(F) > 0:
            node = F.pop(0)
            Ex.add(node)
            metrics.nodes_expanded +=1

            if node.__eq__(GOAL_STATE):
                print ("encontrado")
                metrics.success = True
                metrics.frontier = len(F)
                print(node.get_trace())
                t1_stop = perf_counter() 
                metrics.time = (t1_stop-t1_start)
                metrics.depth = node.depth
                return metrics
            
            moves = possible_moves(node.matrix, node.blankspace)
            
            for move in moves:
                nextNode = next(node.matrix, node.blankspace, move, node)
                if nextNode not in Ex:
                    F.append(nextNode)
                    A.append(nextNode)
                    
            F.sort(key=self.f)

        print("no encontrado")
        t1_stop = perf_counter() 
        metrics.time = (t1_stop-t1_start)
        metrics.depth = node.depth
        metrics.success = False
        return metrics