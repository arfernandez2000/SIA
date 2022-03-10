from node import Node
import copy
import random

FINAL_MATRIX = [[1,2,3], [4,5,6], [7,8,0]]
matrix = []

def read_matrix (filename):
    f = open(filename, "r")
    map = f.readline()
    index = 0
    for i in range(len(FINAL_MATRIX[0])):
        row = []
        for j in range(len(FINAL_MATRIX)):
            row.append(int(map[index]))
            index = index + 1
        matrix.append(row)
    return matrix
    f.close()

def fill_matrix ():
    options = []
    matrix = []
    max = len(FINAL_MATRIX) * len(FINAL_MATRIX)
    for i in range(max):
        options.append(i)
    for i in range(len(FINAL_MATRIX[0])):
        row = []
        for j in range(len(FINAL_MATRIX)):
            index = random.randint(0, len(options)-1)
            print(len(options), index, options[index])
            row.append(options[index])
            options.pop(index)
        matrix.append(row)
    return matrix

def check_move (row, column, matrix):
    len_row = len(matrix)
    len_col = len(matrix[0])
    if row < 0 or column < 0 or row >= len_row or column >= len_col:
        return False
    return True

def next(mat, empty_tile_pos, new_empty_tile_pos, previous):
   
    new_mat = copy.deepcopy(mat)
    
    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]

    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
        
    depth = previous.depth + 1
    
    return Node(new_mat, previous, new_empty_tile_pos, depth)

def possible_moves(mat, empty_tile_pos):
    moves = []
    
    if check_move(empty_tile_pos[0] + 1, empty_tile_pos[1], mat):
        moves.append([empty_tile_pos[0] + 1, empty_tile_pos[1]])

    if check_move(empty_tile_pos[0] - 1, empty_tile_pos[1], mat):
        moves.append([empty_tile_pos[0] - 1, empty_tile_pos[1]])

    if check_move(empty_tile_pos[0], empty_tile_pos[1] + 1, mat):
        moves.append([empty_tile_pos[0], empty_tile_pos[1] + 1])

    if check_move(empty_tile_pos[0], empty_tile_pos[1] - 1, mat):
        moves.append([empty_tile_pos[0], empty_tile_pos[1] - 1])
        
    return moves

def get_inv_count(arr):
    inv_count = 0
    empty_value = -1
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
def is_solvable(matrix) :
    
    inv_count = get_inv_count([j for sub in matrix for j in sub])

    return (inv_count % 2 == 0)                                                                    