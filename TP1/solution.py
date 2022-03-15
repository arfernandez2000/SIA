from node import Node
import copy
import random

FINAL_MATRIX = [1,2,3,4,5,6,7,8,0]
GOAL_STATE = Node(FINAL_MATRIX, None, None, None)

matrix = []

def get_blanckspace(matrix):
    for i in range(len(FINAL_MATRIX)):
        if matrix[i] == 0:
            return i

def read_matrix (filename):
    f = open(filename, "r")
    map = f.readline()
    index = 0
    for i in range(len(FINAL_MATRIX)):
        matrix.append(int (map[index]))
        index = index + 1
    f.close()
    blanskspace = get_blanckspace(matrix)
    return Node(matrix, None,blanskspace, 0)

def get_inv_count(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def is_solvable(matrix) :
    inv_count = get_inv_count(matrix)

    return (inv_count % 2 == 0)   

def fill_matrix ():
    options = []
    matrix = []
    max = len(FINAL_MATRIX) * len(FINAL_MATRIX)
    solvable = False
    while not solvable:
        for i in range(max):
            options.append(i)
        for i in range(len(FINAL_MATRIX[0])):
            row = []
            for j in range(len(FINAL_MATRIX)):
                index = random.randint(0, len(options)-1)
                row.append(options[index])
                options.pop(index)
            matrix.append(row)
        solvable = is_solvable(matrix)
        if not solvable:
            matrix = []
            options = []
    blankspace = get_blanckspace(matrix)
    return Node(matrix, None, blankspace, 0)

def check_move (new_position, matrix):
    if new_position < 0 or new_position >= len(matrix):
        return False
    return True

def next(mat, empty_tile_pos, new_empty_tile_pos, previous):
   
    new_mat = copy.deepcopy(mat)

    x1 = new_mat[empty_tile_pos]
    x2 = new_mat[new_empty_tile_pos]
    
    new_mat[empty_tile_pos] = x2
    new_mat[new_empty_tile_pos] = x1
        
    depth = previous.depth + 1
    
    return Node(new_mat, previous, new_empty_tile_pos, depth)

def possible_moves(mat, empty_tile_pos):
    moves = []
    
    if check_move(empty_tile_pos + 3, mat):
        moves.append(empty_tile_pos + 3)

    if check_move(empty_tile_pos - 3, mat):
        moves.append(empty_tile_pos - 3)

    if(empty_tile_pos % 3 != 2): #derecha
        moves.append(empty_tile_pos + 1)

    if(empty_tile_pos % 3 != 0): #izquierda
        moves.append(empty_tile_pos - 1)
 
    return moves
