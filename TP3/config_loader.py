import numpy
import json

f = open('config.json')
data = json.load(f)
f.close()

operation = data['operation']
trainData = numpy.array([[-1,1,1], [1,-1,1], [-1,-1,1] , [1,1,1]])
expectOut = []

if operation == 'and':
    expectOut = numpy.array([-1,-1,-1,1])
else:
    expectOut = numpy.array([1,1,-1,-1])

perceptron = data['perceptron']
def load_entries():
    f = open('./entries_2.txt', 'r')
    line = f.readline()
    entries = []
    while line:
        entrie = (line.strip('\n')).split('   ')[1:]
        entrie = list(map(lambda x: float(x), entrie))
        entries.append(entrie)
        line = f.readline()
    f.close()
    return entries

def load_goals():
    f = open('./expected_output_2.txt', 'r')
    line = f.readline()
    goals = []
    while line:
        goals.append(float(line.strip(' ')))
        line = f.readline()
    f.close()
    return goals

entries = load_entries()
goals = load_goals()