import math

def heu_wrong_row_col(node):
    heu = 0
    matrix = node.matrix
    side_size = math.sqrt(len(matrix))
    for i in range(len(matrix)):
        if (i % side_size != matrix[i-1] % side_size):
            heu = heu + 1
        if matrix[i] == 0:
            if i < (len(matrix) - side_size):
                heu = heu + 1
        else:
            div_i = math.floor(i/side_size)
            div_pos = math.floor((matrix[i]-1)/side_size)
            if(div_i != div_pos):
                heu = heu + 1
    return heu

def heu_wrong_tile(node):
    heu = 0
    matrix = node.matrix
    for i in range(len(matrix) - 1):
        if matrix[i] != i + 1:
            heu += 1

    if matrix[len(matrix) - 1] != 0:
        heu += 1
    return heu

