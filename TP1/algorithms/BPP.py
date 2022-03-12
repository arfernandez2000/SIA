from algorithms.search import search
from algorithms.search import get_depth
from metrics import Metrics

def bpp(root_node):
    metrics = Metrics('BPP', False, 0,0,0,0)
    return search(root_node, metrics)