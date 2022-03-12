from metrics import Metrics
from algorithms.search import search
from algorithms.search import get_depth

def bpa(root_node):
    metrics = Metrics('BPA', False,  0,0,0,0)
    return search(root_node, metrics,  False)