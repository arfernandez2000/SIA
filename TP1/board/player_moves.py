from node import Node
from box_moves import check_move_box
from box_moves import get_boxes_pos
from board import LEFT
from board import RIGHT
from board import UP
from board import DOWN

def get_moves(board, node, checkDeadlocks = False):
        moves = []

        player_left = (node.player[0] - 1, node.player[1])
        player_right = (node.player[0] + 1, node.player[1])
        player_up = (node.player[0], node.player[1] + 1)
        player_down = (node.player[0], node.player[1] - 1)

        check_move(board, moves, node, player_left, LEFT, checkDeadlocks)
        check_move(board, moves, node, player_right, RIGHT, checkDeadlocks)
        check_move(board, moves, node, player_up, UP, checkDeadlocks)
        check_move(board, moves, node, player_down, DOWN, checkDeadlocks)

        return moves

def check_move(board, moves, node, new_position, direction, checkDeadlocks):
    
    if(new_position not in board.walls):
            
        if(new_position in node.boxes): 
            boxes_copy = node.boxes.copy()
            boxes_copy.remove(new_position)
            if(check_move_box(board, boxes_copy, new_position, direction, checkDeadlocks)): 
                moves.append(Node(new_position, get_boxes_pos(node.boxes, direction, new_position), node, direction, node.depth + 1))
        else: 
            moves.append(Node(new_position, node.boxes, direction, node, node.depth + 1))