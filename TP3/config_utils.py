import numpy
import re

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
            pass
        i += 1
    return numbers
