import numpy
import json

f = open('config.json')
data = json.load(f)
f.close()

operation = data['operation']
trainDataEx1 = numpy.array([[-1,1,1], [1,-1,1], [-1,-1,1] , [1,1,1]])
expectOutEx1 = []

if operation == 'and':
    expectOutEx1 = numpy.array([-1,-1,-1,1])
else:
    expectOutEx1 = numpy.array([1,1,-1,-1])

perceptron = data['perceptron']
def load_entries(filename):
    f = open(filename, 'r')
    line = f.readline()
    entries = []
    while line:
        entrie = (line.strip('\n')).split('   ')[1:]
        entrie = list(map(lambda x: float(x), entrie))
        entries.append(entrie)
        line = f.readline()
    f.close()
    return entries

def load_goals(filename):
    f = open(filename, 'r')
    line = f.readline()
    goals = []
    while line:
        goals.append(float(line.strip(' ')))
        line = f.readline()
    f.close()
    return goals

trainDataEx2 = load_entries('./entries_2.txt')
expectOutEx2 = load_goals('./expected_output_2.txt')

# test_trainDataEx2 = load_entries('./test_entries_2.txt')
# test_expectOutEx2 = load_goals('./test_outputs_2.txt')