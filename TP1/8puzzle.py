from node import Node
from algorithms.BPA import bpa
from algorithms.BPP import bpp
from algorithms.BPPV import search_BPPV
from algorithms.search import search
from solution import fill_matrix
from solution import read_matrix
from mapException import MapException

try:
    print ("ARRANCO")
    root_node = read_matrix("maps/map_solution.txt")
    print("matriz inicial: ", root_node.matrix)
    search_BPPV(root_node)
    print("hola mundo")
except MapException as e:
    print(str(e))