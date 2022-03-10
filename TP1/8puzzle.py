from node import Node

from mapException import MapException

try:
    print("hola")
except MapException as e:
    print(str(e))