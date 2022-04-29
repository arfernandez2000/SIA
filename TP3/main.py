#import numpy
from perceptrons.NonLinearSimplePerceptron import *
from perceptrons.Perceptron import *
from perceptrons.StepSimplePerceptron import *
from perceptrons.LinearSimplePerceptron import *
from config_loader import *
from plot_step_simple import plot as plot_step
from plot_errors import plot as plot_errors

if perceptron == "non-linear":
    #non_linear_perceptron = NonLinearSimplePerceptron(trainDataEx2[:150], expectOutEx2[:150], 0.005, 0.5)
    non_linear_perceptron = NonLinearSimplePerceptron(trainDataEx2, expectOutEx2, 0.1, 0.5)
    non_linear_perceptron.train(50000)
    plot_errors()
    #non_linear_perceptron.test(trainDataEx2[150:], expectOutEx2[150:])

elif perceptron == "linear":
    linear_perceptron = LinearSimplePerceptron(test_trainDataEx2, test_expectOutEx2, 0.01)
    linear_perceptron.train(1000)
    plot_errors()

else:
    perceptron = StepSimplePerceptron(trainDataEx1, expectOutEx1, 0.01)
    perceptron.train(1000)
    plot_step()