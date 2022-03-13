from abc import ABC, abstractmethod
class Search(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def search(self, root_node):
        pass

    def get_depth(self, nodes):
        return nodes.depth