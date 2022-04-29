from abc import ABC


import numpy as np

class MultilayerPerceptron(ABC):
    def __init__(self, training, output, learningRate) -> None:
        super().__init__()

    def train(self):
        w = np.random.rand(len(self.train))