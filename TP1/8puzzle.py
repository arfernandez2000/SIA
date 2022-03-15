from node import Node
from algorithms.BPA import BPA
from algorithms.BPP import BPP
from algorithms.BPPV import BPPV
from algorithms.heu_local import LocalHeuristic
from algorithms.heu_global import GlobalHeuristic
from algorithms.A_star import AStar
from algorithms.search import Search
from solution import is_solvable
from solution import read_matrix
from heu import heu_wrong_tile, heu_wrong_row_col, heu_linear_distance
from mapException import MapException
from web import render
import json

def choose_heuristic(argument):
  switcher = {
       "tile": heu_wrong_tile,
       "rowcol": heu_wrong_row_col,
       "linear": heu_linear_distance, 
  }

  return switcher.get(argument, "Wrong heuristic!")

def choose_search_method(argument):
    switcher = {
        "BPA": BPA(),
        "BPP": BPP(),
        "BPPV": BPPV(),
        "LOCAL_H": LocalHeuristic(),
        "GLOBAL_H": GlobalHeuristic(),
        "A_STAR": AStar()
    }
    
    return switcher.get(argument, "Wrong search method!")

def getMethod(data):
    methodName = ""

    for i in data["method"]:
        methodName = methodName + i
    
    return choose_search_method(methodName)

def getMap(data):
    mapName = ""
    for i in data["map"]:
        mapName = mapName + i
    return mapName

def getHeu(data):
    heuristicName = ""
    for i in data["heuristic"]:
        heuristicName = heuristicName + i
    heu = choose_heuristic(heuristicName)
    return heu

def getData():
    f = open('config.json')
    data = json.load(f)

    search_method = getMethod(data)
    mapName = getMap(data)

    informed = data["informed"]
    if informed:
        heu = getHeu(data)
        search_method.setHeuristic(heu)

    f.close()

    return mapName, search_method

try:
    mapName, search_method = getData()
    root_node = read_matrix(mapName)
    if(not is_solvable(root_node.matrix)):
        raise Exception('Matrix not solvable')
    if (isinstance(search_method, str)):
        raise Exception(search_method)
    answer = search_method.search(root_node)

    render(answer)
except MapException as e:
    print(str(e))