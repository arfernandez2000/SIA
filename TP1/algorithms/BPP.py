from metrics import Metrics
from logging import root
from metrics import Metrics
from time import perf_counter
from solution import GOAL_STATE
from solution import possible_moves
from solution import next
from algorithms.search import Search

class BPP(Search):
    def __init__(self):
        super().__init__()
        self.metrics = metrics = Metrics('BPP')

    def search(self, root_node):
        t1_start = perf_counter()
        A = []
        F = []
        Ex = set()
        metrics = self.metrics
        F.append(root_node)
        A.append(root_node)

        while len(F) > 0:
            node = F.pop()
            print ("NODE ", node.matrix)
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
                metrics.goal = node
                return metrics
            
            moves = possible_moves(node.matrix, node.blankspace)
            
            for move in moves:
                nextNode = next(node.matrix, node.blankspace, move, node)
                if nextNode not in Ex:
                    F.append(nextNode)
                    A.append(nextNode)


        print("no encontrado")
        t1_stop = perf_counter() 
        metrics.time = (t1_stop-t1_start)
        metrics.depth = node.depth
        metrics.success = False
        return metrics