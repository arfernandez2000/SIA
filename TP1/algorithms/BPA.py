from search import search
import get_depth
from solution import INITIAL_STATE

def bpa(root_node):
    search(root_node, get_depth, True)

bpa(INITIAL_STATE)