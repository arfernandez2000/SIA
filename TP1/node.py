class Node:
    def __init__ (self, matrix, previous, blankSpace, depth, heuristic):
        self.matrix = matrix
        self.depth = depth
        self.heu = heuristic
        self.prev = previous
        self.blankSpace = blankSpace
 
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for i in range(len(self.matrix[0])):
                for j in range(len(self.matrix)):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        return False

    def _eq_BPPV_(self, other):
        if self.depth > other.depth:
            return False
        return self.__eq__(self, other)

    def __hash__(self):
        return hash((self.matrix))

    def __str__(self):
        for i in range(len(self.matrix[0])):
                for j in range(len(self.matrix)):
                    print(self.matrix[i][j])