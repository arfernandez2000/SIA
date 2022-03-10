from solution import GOAL_STATE

def search(root_node, sort_key = get_depth, reverse = True):
    A = [root_node]
    F = [root_node]
    Ex = []

    while len(F) > 0:
        node = F.pop(0)
        Ex.append(node)

        if node.__eq__(GOAL_STATE):
            return "encontrado"
        
        moves = possible_moves(node.matrix, node.blankSpace)

        for move in moves:
            if move not in Ex:
                F.append(move)
                A.append(move)
    
    F.sort(sort_key, reverse)
    
    return "no encontrado"

def get_depth(nodes):
    return nodes.depth