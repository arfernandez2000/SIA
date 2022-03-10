from node import Node
from board.board import Board
from mapException import MapException

try:
    board = Board('soko_1.txt')
    print("hola")
    print(board.get_moves_board(Node(board.player, board.boxes, None, None, 0)))
except MapException as e:
    print(str(e))