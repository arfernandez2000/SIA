#import numpy
from perceptrons.NonLinearSimplePerceptron import *
from perceptrons.Perceptron import *
from perceptrons.StepSimplePerceptron import *
from perceptrons.LinearSimplePerceptron import *
from config_loader import *
from plot_step_simple import plot as plot_step
from plot_linear_errors import plot as plot_linear

print(perceptron)
if perceptron == "non-linear":
    non_linear_perceptron = NonLinearSimplePerceptron(trainDataEx2, expectOutEx2, 0.01, 0.4)
    non_linear_perceptron.train(5000)

elif perceptron == "linear":
    linear_perceptron = LinearSimplePerceptron(test_trainDataEx2, test_expectOutEx2, 0.01)
    linear_perceptron.train(1000)
    plot_linear()

else:
    perceptron = StepSimplePerceptron(trainDataEx1, expectOutEx1, 0.01)
    perceptron.train(1000)
    plot_step()