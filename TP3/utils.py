from math import trunc
import math
import numpy as np
import random

def lineal_act(x):
    return x

def der_lineal_act(x):
    return 1

def tanh_act(x):
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
    print('SPLITS A', splitsA)
    print('len splits a, ', len(splitsA))
    splitsE = truncate(expected, K)
    print('SPLITS E', splitsE)
    print('len splits e, ', len(splitsE))
    testId = random.randint(0, K-1)
    print('TEST ID: ', testId)
    test = splitsA[testId]
    print('TEST: ', test)
    testExp = splitsE[testId]
    print('TEST EXP: ', testExp)
    print('len test: ', len(test))
    print('len test exp: ', len(testExp))
    train = []
    trainExp = []
    for i in range(K):
        if i != testId:
            for num in splitsA[i]:
                train.append(num)
            for num in splitsE[i]:
                trainExp.append(num)
    return train, trainExp, test, testExp, testId
