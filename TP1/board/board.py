import imp
from mapException import MapException
from node import Node
from player_moves import *

LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

class Board:
    def __init__(self, filename):
        file = open(filename, "r")
        self.walls = set()
        self.boxes = set()
        self.goals = set()
        self.player = None
        self.max_point = self.fill_board(file)
    

    def fill_board(self, file):
        lines = [line.strip("\n") for line in file if line != "\n"]
        x=0
        y=0
        max_x=0
        for line in lines:
            x=0
            for char in line:
                if(char == "#"):
                    self.walls.add((x,y))
                elif (char == "." ):
                    self.goals.add((x,y))
                elif (char == "$"):
                    self.boxes.add((x,y))
                elif (char == "@"):
                    self.player = (x,y)
                x+=1
                if(x > max_x):
                    max_x = x
            y+=1
        if (len(self.boxes) == 0): raise MapException("ERROR: Map must have one box")
        if (len(self.goals) == 0): raise MapException("ERROR: Map must have one goal")
        elif (len(self.boxes) != len(self.goals)): raise MapException("ERROR: Map must have the same amount of goals and boxes")
        return (max_x -1, y-1)


    def isCompleted(self, node):
        for box in node.boxes:
            if box not in self.goals:
                return False
        return True

    def get_moves_board(self, node, checkDeadlocks = False):
        player_moves.get_moves(self, node, checkDeadlocks = False)



    