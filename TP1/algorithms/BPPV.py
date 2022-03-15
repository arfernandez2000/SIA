from metrics import Metrics
from solution import GOAL_STATE
from solution import possible_moves
from solution import next
from algorithms.search import Search
from time import perf_counter

class BPPV(Search):
    F = []
    depth = 0
    def __init__(self):
        super().__init__()
        self.metrics = metrics = Metrics('BPPV')
        self.LIMIT_INCREASE = 25

    def search(self, root_node):

        t1_start = perf_counter()
        metrics = self.metrics
        final_node = self.bppv(root_node) 
            
        if(final_node is True):
            metrics.success = True 
            metrics.frontier = len(self.F)
            t1_stop = perf_counter() 
            metrics.time = (t1_stop-t1_start)
            metrics.depth = self.depth
            return metrics
        
        t1_stop = perf_counter() 
        metrics.time = (t1_stop-t1_start)
        metrics.depth = self.depth
        metrics.success = False
        return metrics
    
        
    def bppv(self, root_node):

        A = []
        F = self.F
        Ex = set()

        F.append(root_node)
        start = 0
        i = 0
        limit = self.LIMIT_INCREASE
        last_level_nodes = []

        while F:
            while F:
                result = self.bppv_rec(F, A, Ex, start, limit, last_level_nodes)
                if(result is True):
                    return result
            start = limit
            limit += self.LIMIT_INCREASE
            F = last_level_nodes.copy()
            last_level_nodes = []
            i += 1
        # NO SOLUTION
        self.metrics.success = False
        return False
        
    def bppv_rec(self, F, A, Ex, start, limit, last_level_nodes):
        node = F.pop()
        if node.__eq__(GOAL_STATE):
            self.depth = node.depth
            self.metrics.goal = node
            return True

        if(start == limit): #reached max_depth and sn not found
            last_level_nodes.insert(0,node)
            return False

        Ex.add(node)
        self.metrics.nodes_expanded += 1
        
        moves = possible_moves(node.matrix, node.blankspace)

        for move in moves:
            nextNode = next(node.matrix, node.blankspace, move, node)
            if(nextNode not in Ex):
                F.append(nextNode)
                result = self.bppv_rec(F, A, Ex, start + 1, limit, last_level_nodes)
                if(result is not False):
                    self.F = F
                    return result   
        self.F = F
        return False