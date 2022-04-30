from cgi import test
from locale import normalize
import numpy
import json
import re

f = open('config.json')
data = json.load(f)
f.close()

operation = data['operation']
trainDataEx1 = numpy.array([[-1,1,1], [1,-1,1], [-1,-1,1] , [1,1,1]])
expectOutEx1 = []
expectOutEx32 = [1,-1,1,-1,1,-1,1,-1,1,-1]


if operation == 'and':
    expectOutEx1 = numpy.array([-1,-1,-1,1])
else:
    expectOutEx1 = numpy.array([1,1,-1,-1])

perceptron = data['perceptron']

def load_entries(filename, row):
    f = open(filename, 'r')
    line = f.readline()
    entries = []
    while line:
        if row > 1:
            aux = numpy.array([])
            for i in range(0,row):
                entrie = (line.strip('\n')).split(' ')[:-1]
                entrie = list(map(lambda x: float(x), entrie))
                aux = numpy.append(entrie, aux)
                line = f.readline()
            entries.append(aux)
        else:
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

trainDataEx2 = load_entries('./entries_2.txt', 1)
expectOutEx2 = load_goals('./expected_output_2.txt')

test_trainDataEx2 = load_entries('./test_entries_2.txt', 1)
test_expectOutEx2 = load_goals('./test_outputs_2.txt')

trainDataEx3 = load_entries('./entries_3.txt', 7)

def parse_data(path):
    file = open(path, "r")
    lines = file.readlines()

    matrix = []
    count = 0
    for line in lines:
        count += 1
        aux = re.split("\s+", line)
        if aux[0] == "":
            aux.pop(0)
        if aux[len(aux) - 1] == "":
            aux.pop()
        matrix.append(stringToNum(aux))
    return matrix

def stringToNum(matrix):
    aux = []
    for string in matrix:
        aux.append(float(string))
    return aux

def parseNumbers(path):
    file = open(path, "r")
    lines = file.read()
    length = len(lines)
    numbers = []
    auxMatrix = []
    i = 0
    line = 0

    while i < length:
        if lines[i] == "0":
            auxMatrix.append(0)
        elif lines[i] == "1":
            auxMatrix.append(1)
        elif lines[i] == "\n":
            if line == 6:
                line = 0
                numbers.append(auxMatrix)
                auxMatrix = []
            else:
                line += 1
        else:  # es un " "
            pass
        i += 1
    return numbers
