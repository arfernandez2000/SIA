from perceptrons.StepSimplePerceptron import StepSimplePerceptron
from config_loader import trainData, expectOut
from plot_step_simple import plot

def ex1():
    perceptron = StepSimplePerceptron(trainData, expectOut, 0.2)
    w, errs = perceptron.train(1000)
    plot(w)