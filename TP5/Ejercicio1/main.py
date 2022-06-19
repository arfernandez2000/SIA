import csv
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import random
from sys import stdout
from math import exp, floor
import parser
from network import Network
from constants import ModeOptions
from utils import createNoise, predictAndPrintResults, concatenateArrays
from graphing import plotLatentSpace

CONFIG_INPUT = "configuration.json"
labels = ['@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_']

def trainMultilayer(config, inputs):
    network = Network(config, inputs.shape[1])
    latent, latentLabels = network.train(inputs, inputs, labels)
    if len(config.generatorPoints) > 0:
        results = network.generate(config.generatorPoints)
        results = [[r[0], np.array([1 if e > 0.5 else 0 for e in r[1]]).reshape((7, 5))] for r in results]
        for result in results:
            print(f'Generated using {result[0]}:\n {result[1]}')
        plotLatentSpace(latent,latentLabels,generated = results)
    return network

def trainMultilayerOptimizer(config, inputs, optimizer):
    network = Network(config, inputs.shape[1])
    error = network.trainMinimizer(inputs, optimizer)

def predictNewNoise(config, network, expected):
    print('#### NEW SET RESULTS ####')

    newNoiseInputs = np.array([createNoise(origInput, config.noiseProbability) for origInput in expected])

    inputs = concatenateArrays(newNoiseInputs, expected)
    outputs = concatenateArrays(expected, expected)

    predictAndPrintResults(network, inputs, outputs)


def main():
    config = parser.parseConfiguration(CONFIG_INPUT)    

    print("######################\nTRAINING\n######################")
    if config.mode == ModeOptions.NORMAL.value:
        inputs = parser.parseInput(config.input)
        trainMultilayer(config, inputs)
    else:
        inputs = parser.parseInput(config.input)
        trainMultilayerOptimizer(config, inputs, config.optimizer)

if __name__ == "__main__":
    main()