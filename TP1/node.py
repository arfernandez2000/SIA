class Node:
    def __init__ (self, player, boxes, direction, previous, depth, heuristic):
        self.player = player
        self.boxes = boxes
        self.direction = direction
        self.depth = depth
        self.heu = heuristic
        self.prev = previous
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and other.player == self.player and other.boxes == self.boxes)

    def __hash__(self):
        return hash((self.player,self.boxes))