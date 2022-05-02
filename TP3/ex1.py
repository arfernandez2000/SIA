from perceptrons.StepSimplePerceptron import StepSimplePerceptron
from config_loader import trainDataEx1, expectOutEx1
from plot_step_simple import plot

def ex1():
    perceptron = StepSimplePerceptron(trainDataEx1, expectOutEx1, 0.2)
    perceptron.train(1000)
    plot()