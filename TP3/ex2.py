import numpy as np
from perceptrons.NonLinearSimplePerceptron import *
from plot_accuracies import plot_acc
from utils import *
from config_loader import *
from utils import *
from config_utils import parse_data
from plot_errors import plot_list_error
from perceptrons.LinearSimplePerceptron import *

def ex2():
    if expoint == 1:
        ex2_1()
    elif expoint == 2:
        ex2_2()
    elif expoint == 3:
        ex2_3()

def ex2_1():
    linear_perceptron = LinearSimplePerceptron(trainData, expectOut, 0.01)
    w, errors = linear_perceptron.train(10000)
    plot_list_error(errors)

def ex2_2():
    i = 0
    max_value = np.max(expectOut)
    min_value = np.min(expectOut)
    expected_matrix_normalized = np.zeros(len(expectOut))
    while i < len(expectOut):
        expected_matrix_normalized[i] = ((expectOut[i][0] - min_value) / (max_value - min_value))
        i += 1
    perceptron_nolineal2 = NonLinearSimplePerceptron(np.array(trainData).shape[1], logist, der_logist, eta=0.01)
    min_err, epochs, error_list, training_accuracies, min_err_test, test_accuracies = perceptron_nolineal2.train(trainData, expected_matrix_normalized, [], [], 0.001)

    print()
    print("training error", min_err)
    print("max training accuracy", training_accuracies[-1])
    print()

    plot_list_error(error_list)
    plot_list_error(training_accuracies)

def ex2_3():
    i = 0
    max_value = np.max(expectOut)
    min_value = np.min(expectOut)
    expected_matrix_normalized = np.zeros(len(expectOut))
    while i < len(expectOut):
        expected_matrix_normalized[i] = ((expectOut[i][0] - min_value) / (max_value - min_value))
        i += 1

    len_training = len(trainData)
    training_set, training_expected, test_set, test_expected, testID = cross_validations(trainData, expected_matrix_normalized, 8)
    training_set = np.array(training_set)
    training_expected = np.array(training_expected)
    test_set = np.array(test_set)
    test_expected = np.array(test_expected)
    after_len = len(training_set)
    

    perceptron_nolineal2 = NonLinearSimplePerceptron(training_set.shape[1], logist, der_logist, eta=0.01)
    min_err, epochs, error_list, training_accuracies, min_err_test, test_accuracies = perceptron_nolineal2.train(training_set, training_expected, test_set, test_expected, 0.001)
    min_err_test, test_accuracies = perceptron_nolineal2.test(test_set, test_expected)

    print()
    print("training error", min_err)
    print("testing error", min_err_test)
    print("porcentaje de training", after_len*100/len_training)
    print()

    plot_list_error(error_list)

