from solution import GOAL_STATE
from solution import possible_moves
from solution import next

LIMIT_INCREASE = 25

def search_BPPV(root_node):
        
    final_node = iddfs(root_node) 
        
    if(final_node is True):
        print("enoctradoo")
        return
        # self.metrics.success = True 
        # self.metrics.frontier = len(self.queue) + len(self.last_level_nodes)
        # return SearchResults(self.metrics, final_node)
            
    #self.metrics.success = False
    print("no enoctradoo")
    return 
   
    
def iddfs(root_node):

    A = []
    F = []
    Ex = set()

    F.append(root_node)
    start = 0
    i = 0
    limit = LIMIT_INCREASE
    last_level_nodes = []

    while F:
        print("primer while")
        while F:
            print("segundo while")
            result = iddfs_rec(F, A, Ex, start, limit, last_level_nodes)
            if(result is True):
                print("encontrado")
                return result
        start = limit
        limit += LIMIT_INCREASE
        print("nuevo limite", limit)
        F = last_level_nodes.copy()
        last_level_nodes = []
        i += 1
    # NO SOLUTION
    #self.metrics.success = False
    return False
    
def iddfs_rec(F, A, Ex, start, limit, last_level_nodes):
    node = F.pop()
    #print("NODE", node.matrix)  
    if node.__eq__(GOAL_STATE):
        print ("encontrado")
        print(node.matrix)
        return True

    if(start == limit): #reached max_depth and sn not found
        print("Llegue al limite", node.depth)
        last_level_nodes.insert(0,node)
        return False

    Ex.add(node)
    #self.metrics.nodes_expanded += 1
       
    moves = possible_moves(node.matrix, node.blankspace)

    for move in moves:
        nextNode = next(node.matrix, node.blankspace, move, node)
        if(nextNode not in Ex):
            print(nextNode.matrix)
            F.append(nextNode)
            result = iddfs_rec(F, A, Ex, start + 1, limit, last_level_nodes)
            if(result is not False):
                return result
    print("F despues d la recu", len(F))     
    return False