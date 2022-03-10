from search import search
from search import get_depth

def bpp(root_node):
    search(root_node, get_depth, False)