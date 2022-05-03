import numpy as np
from perceptrons.NonLinearSimplePerceptron import *
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
    w, errors = linear_perceptron.train(50000)
    plot_list_error(errors)

def ex2_2():
    perceptron_nolineal2 = NonLinearSimplePerceptron(len(trainData), tanh_act, der_tanh_act, eta=0.01)
    min_err, epochs, error_list, training_accuracies, min_err_test, test_accuracies = perceptron_nolineal2.train(trainData, expectOut, [], [], 0.001)

    print()
    print("training error", min_err)
    print()

    plot_list_error(error_list)

def ex2_3():
    i = 0
    max_value = np.max(expectOut)
    min_value = np.min(expectOut)
    expected_matrix_normalized = np.zeros(len(expectOut))
    while i < len(expectOut):
        expected_matrix_normalized[i] = 2 * ((expectOut[i][0] - min_value) / (max_value - min_value)) - 1
        i += 1

    training_set, training_expected, test_set, test_expected, testID = cross_validations(trainData, expected_matrix_normalized, 3)
    training_set = np.array(training_set)
    training_expected = np.array(training_expected)
    test_set = np.array(test_set)
    test_expected = np.array(test_expected)

    perceptron_nolineal2 = NonLinearSimplePerceptron(training_set.shape[1], tanh_act, der_tanh_act, eta=0.01)
    min_err, epochs, error_list, training_accuracies, min_err_test, test_accuracies = perceptron_nolineal2.train(training_set, training_expected, test_set, test_expected, 0.001)
    min_err_test, test_accuracies = perceptron_nolineal2.test(test_set, test_expected)

    print()
    print("training error", min_err)
    print("testing error", min_err_test)
    print()

    plot_list_error(error_list)

    # def cross_validations(array, expected, K):
    #     splitsA = truncate(array, K)
    #     splitsE = truncate(expected, K)
    #     testId = random.randint(0, K-1)
    #     test = splitsA[testId]
    #     testExp = splitsE[testId]

    #     train = []
    #     trainExp = []
    #     for i in range(K):
    #         if i != testId:
    #             for num in splitsA[i]:
    #                 train.append(num)
    #             for num in splitsE[i]:
    #                 trainExp.append(num)
    #     return train, trainExp, test, testExp