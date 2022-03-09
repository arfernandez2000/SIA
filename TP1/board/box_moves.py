from typing_extensions import Self
from board import LEFT
from board import RIGHT
from board import UP
from board import DOWN

def check_deadlock(board, move_box, boxes, checkDeadlocks) :
        if(move_box not in board.walls and move_box not in boxes):
            if(checkDeadlocks and not (move_box in board.goals)): # deadlock check turned on

                    aux_left = (move_box[0]-1, move_box[1])
                    aux_right = (move_box[0]+1, move_box[1])
                    aux_up = (move_box[0], move_box[1]+1)
                    aux_down = (move_box[0], move_box[1]-1)

                    if(aux_up in board.walls or aux_up in boxes or aux_down in board.walls or aux_down in boxes):
                        if(aux_left in board.walls or aux_left in boxes or aux_right in board.walls or aux_right in boxes):
                            return False

            return True
                
        return False # deadlock check turned off

def check_move_box(board, boxes, player, direction, checkDeadlocks):
    if (direction == UP):
        move_box = (player[0], player[1] + 1)
    elif( direction == DOWN):
        move_box = (player[0], player[1]-1)
    elif (direction == LEFT):
        move_box = (player[0]-1, player[1])
    else:
        move_box = (player[0]+1, player[1])
    board.check_deadlock(board, move_box, boxes, checkDeadlocks)

def get_boxes_pos(boxes, player_pos, direction):
    boxes = set()
    for b in boxes: 
        if(b == player_pos):
            aux = list(b)
              
            if(direction == LEFT):
                aux[0] = player_pos[0] - 1
            elif(direction == RIGHT):
                aux[0] = player_pos[0] + 1
            elif(direction == UP):
                aux[1] = player_pos[1] + 1 
            elif(direction == DOWN):
                aux[1] = player_pos[1] - 1
                
            b = tuple(aux)

        boxes.add(b)
    return boxes
