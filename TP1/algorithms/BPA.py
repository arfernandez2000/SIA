from solution import *

def sort_BPA(nodes):
    return nodes.depth

def bpa(root_node):
    A = [root_node]
    F = [root_node]
    Ex = []

    while len(F) > 0:
        node = F[0]
        Ex.append[node]

        if node == FINAL_MATRIX:
            return "encontrado"
        
        moves = possible_moves(node.matrix, node.blankSpace)

        for move in moves:
            if move not in Ex:
                F.append(move)
                A.append(move)
        
        F.sort(key= sort_BPA)
    
    return "no encontrado"


