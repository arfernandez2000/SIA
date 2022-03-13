from metrics import Metrics
#from algorithms.search import get_depth
from logging import root
from metrics import Metrics
from solution import GOAL_STATE
from solution import possible_moves
from solution import next
from algorithms.search import Search

class LocalHeuristic(Search):
    def __init__(self):
        super().__init__()
        self.heumethod = None
        self.metrics = Metrics('LOCAL_H')

    def setHeuristic(self, heu):
        self.heumethod = heu

    def search(self, root_node):
        L = [root_node]
        self.local_heuristic_search(L)

    def local_heuristic_search(self, nodes):
        metrics = self.metrics
        Ex = set()
        while nodes:
            node = nodes.pop(0)
            Ex.add(node)
            print(node.matrix)
            metrics.nodes_expanded +=1

            if node.__eq__(GOAL_STATE):
                print ("encontrado")
                metrics.success = True
                #metrics.frontier = len(A)
                return metrics
            
            moves = possible_moves(node.matrix, node.blankspace)
            for move in moves:
                nextNode = next(node.matrix, node.blankspace, move, node)
                if nextNode not in Ex:
                    nodes.append(nextNode)
            
            nodes.sort(key = self.heumethod)