from cgi import test
from locale import normalize
import numpy
import json
from config_utils import load_entries, load_goals

f = open('config.json')
data = json.load(f)
f.close()

operation = data['operation']
trainDataEx1 = numpy.array([[-1,1,1], [1,-1,1], [-1,-1,1] , [1,1,1]])
expectOutEx1 = []
expectOutEx32 = [1,-1,1,-1,1,-1,1,-1,1,-1]
ex3point = data['multi-layer']['excercise']

if operation == 'and':
    expectOutEx1 = numpy.array([-1,-1,-1,1])
else:
    expectOutEx1 = numpy.array([1,1,-1,-1])

perceptron = data['perceptron']

trainDataEx2 = load_entries('./entries_2.txt', 1)
expectOutEx2 = load_goals('./expected_output_2.txt')

test_trainDataEx2 = load_entries('./test_entries_2.txt', 1)
test_expectOutEx2 = load_goals('./test_outputs_2.txt')

trainDataEx3 = load_entries('./entries_3.txt', 7)