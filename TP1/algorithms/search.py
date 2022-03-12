from logging import root
from metrics import Metrics
from solution import GOAL_STATE
from solution import possible_moves
from solution import next


def get_depth(nodes):
    return nodes.depth

def search(root_node,  metrics, stack = True):
    A = []
    F = []
    Ex = set()

    F.append(root_node)
    A.append(root_node)

    while len(F) > 0:
        
        if stack:
            node = F.pop(0)
        else:
            node = F.pop()
        print ("NODE ", node.matrix)
        Ex.add(node)
        metrics.nodes_expanded +=1

        if node.__eq__(GOAL_STATE):
            print ("encontrado")
            metrics.success = True
            metrics.frontier = len(A)
            return metrics
        
        moves = possible_moves(node.matrix, node.blankspace)
        
        for move in moves:
            nextNode = next(node.matrix, node.blankspace, move, node)
            if nextNode not in Ex:
                F.append(nextNode)
                A.append(nextNode)


    print("no encontrado")

    return metrics