

class Node:
    def __init__ (self, matrix, previous, blankspace, depth, heuristic = None):
        self.matrix = matrix
        self.depth = depth
        self.heu = heuristic
        self.prev = previous
        self.blankspace = blankspace
 
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for i in range(len(self.matrix)):
                if self.matrix[i] != other.matrix[i]:
                    return False
            return True
        return False
    
    def _eq_BPPV_(self, other):
        if self.depth > other.depth:
            return False
        return self.__eq__(self, other)

    def __hash__(self):
        return hash((tuple(self.matrix)))

    def __str__(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def get_trace(self):
        node = self
        trace = []
        i = node.depth
        while(node):
            step = " \n Paso " + str(i) + ": " + str(node.matrix)
            trace.insert(0, step)
            node = node.prev
            i = i-1
        return trace