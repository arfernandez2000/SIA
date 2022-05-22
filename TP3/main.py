from ex3 import ex3
from ex2 import ex2
from ex1 import ex1
from perceptrons.NonLinearSimplePerceptron import *
from perceptrons.Perceptron import *
from perceptrons.StepSimplePerceptron import *
from perceptrons.LinearSimplePerceptron import *

from config_loader import *
from plot_step_simple import plot as plot_step
from plot_errors import plot_list_error, plot as plot_errors

if perceptron == 'multi-layer':
    ex3()

elif perceptron == "non-linear":
    ex2()

elif perceptron == "linear":
    ex2()

else:
    ex1()