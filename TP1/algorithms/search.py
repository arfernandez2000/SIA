from logging import root
from solution import GOAL_STATE
from solution import possible_moves
from solution import next


def get_depth(nodes):
    return nodes.depth

def search(root_node, stack = True):
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

        if node.__eq__(GOAL_STATE):
            print ("encontrado")
            return
        
        moves = possible_moves(node.matrix, node.blankspace)
        
        for move in moves:
            nextNode = next(node.matrix, node.blankspace, move, node)
            if nextNode not in Ex:
                F.append(nextNode)
                A.append(nextNode)


    print("no encontrado")
    return