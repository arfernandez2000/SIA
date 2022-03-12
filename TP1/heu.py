def heu_wrong_tile(node):
    heu = 0
    for i in range(len(node.matrix) - 1):
        if node.matrix[i] != i + 1:
            heu += 1

    if node.matrix[len(node.matrix) - 1] != 0:
        heu += 1
    return heu

def heu_wrong_row_col(node):
    heu = 0
    for i in range(len(node.matrix)):
        if node.matrix[i] == 0:
            if i %3 != 2:
                heu += 1
            if i/3 != 2:
                heu +=1
        elif node.matrix[i] - 1 % 3 != i % 3: #columans
            heu += 1
        if node.matrix[i] <= 3 and i/3 != 0:
            heu += 1
        elif node.matrix[i] >= 7 and i/3 != 2:
            heu += 1
        elif node.matrix[i] > 3 and node.matrix[i] < 7 and i/3 != 1:
            heu += 1
    return heu

