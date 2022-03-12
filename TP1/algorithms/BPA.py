from algorithms.search import search
from algorithms.search import get_depth

def bpa(root_node):
    search(root_node, get_depth, False)