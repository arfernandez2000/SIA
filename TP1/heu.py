import math

def heu_wrong_row_col(matrix):
    heu = 0
    for i in range(len(matrix)):
        if (i % 3 != matrix[i-1] % 3):
            heu = heu + 1
        if matrix[i] == 0:
            if i < 6:
                heu = heu + 1
        else:
            div_i = math.floor(i/3)
            div_pos = math.floor((matrix[i]-1)/3)
            if(div_i != div_pos):
                heu = heu + 1
    return heu
    
def heu_wrong_tile(node):
    heu = 0
    for i in range(len(node.matrix) - 1):
        if node.matrix[i] != i + 1:
            heu += 1

    if node.matrix[len(node.matrix) - 1] != 0:
        heu += 1
    return heu

