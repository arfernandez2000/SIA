from math import trunc
import math
import numpy as np
import random

def tanh_act(x):
    print("TAN:" ,np.tanh(1 * x))
    return np.tanh(1 * x)

def der_tanh_act(x):
    return 1 * (1 - tanh_act(x)**2)

def logist(x):
    return 1 / (1 + math.e**(-2 * 1 * x))

def der_logist(x):
    return 2 * 1 * logist(x) * (1 - logist(x))

def truncate(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def cross_validations(array, expected, K):
    splitsA = truncate(array, K)
    splitsE = truncate(expected, K)
    testId = random.randint(0, K-1)
    test = splitsA[testId]
    testExp = splitsE[testId]

    train = []
    trainExp = []
    for i in range(K):
        if i != testId:
            for num in splitsA[i]:
                train.append(num)
            for num in splitsE[i]:
                trainExp.append(num)
    return train, trainExp, test, testExp, testId
