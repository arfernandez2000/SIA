#import numpy
from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from perceptrons.linearSimplePerceptron import *
from config_loader import *
from plot_step_simple import plot

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

#Con 0.1 se queda corto, no se porque, tendria q llegar igual pero el error da 0 antes
perceptron = perceptrons(trainData, expectOut, 0.001, activationStepSimple, errorStepSimple)
perceptron.train(1000)
plot()

#train = load_entries()
#goals = load_goals()
#linear_perceptron = perceptrons(train,goals,0.001,activatonLinearSimple,errorLinearSimple)
#linear_perceptron.train(1000)
#print(linear_perceptron.wMin, '\nError: ', linear_perceptron.errorMin)