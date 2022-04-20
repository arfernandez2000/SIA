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