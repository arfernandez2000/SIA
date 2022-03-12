from logging import root
from solution import GOAL_STATE
from solution import possible_moves
from solution import next


def get_depth(nodes):
    return nodes.depth

def search(root_node, sort_key = get_depth, reverse = True):
    A = [root_node]
    F = [root_node]
    Ex = []

    while len(F) > 0:
        node = F.pop(0)
        print ("NODE ", node.matrix)
        Ex.append(node)

        if node.__eq__(GOAL_STATE):
            print ("encontrado")
            return
        
        moves = possible_moves(node.matrix, node.blankspace)

        for move in moves:
            nextNode = next(node.matrix, node.blankspace, move, node)
            if nextNode not in Ex:
                F.append(nextNode)
                A.append(nextNode)
        F.sort(key= sort_key, reverse = reverse)

    print("no encontrado")
    return