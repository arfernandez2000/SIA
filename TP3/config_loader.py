from cgi import test
from locale import normalize
import numpy as np
import json
from config_utils import load_entries, load_goals, parse_data

f = open('config.json')
data = json.load(f)
f.close()

expoint = 0
trainData =[]
expectOut =[]

perceptron = data['perceptron']
if perceptron == 'step':
    operation = data['operation']
    trainData = np.array([[-1,1], [1,-1], [-1,-1] , [1,1]])
    if operation == 'and':
        expectOut = np.array([-1,-1,-1,1])
    else:
        expectOut = np.array([1,1,-1,-1])
    trainData = list(map(lambda x: np.append(x,1), trainData)) #umbral anadido
elif perceptron == 'linear':
    linear_input = data['linear_input']['test']
    if linear_input:
        trainData = load_entries('./test_entries_2.txt', 1)
        expectOut = load_goals('./test_outputs_2.txt')
    else:
        trainData = load_entries('./entries_2.txt', 1)
        expectOut = load_goals('./expected_output_2.txt')
    expoint = data['ex2']['excercise']
    trainData = list(map(lambda x: np.append(x,1), trainData)) #umbral anadido
elif perceptron == 'non-linear':
    trainData = parse_data('./entries_2.txt')
    expectOut = parse_data('./expected_output_2.txt')
    expoint = data['ex2']['excercise']
elif perceptron == 'multi-layer':
    expoint = data['ex3']['excercise']
