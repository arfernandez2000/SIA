import numpy as np
from TP3.plot_errors import plot_list_error
from perceptrons.NonLinearSimplePerceptron import *
from utils import *
from config_loader import *
from utils import *
from config_utils import parse_data
from plot_errors import plot as plot_errors, plot_list_erros

training_matrix = parse_data('./entries_2.txt')
expected_matrix = parse_data('./expected_output_2.txt')

i = 0
max_value = np.max(expected_matrix)
min_value = np.min(expected_matrix)
expected_matrix_normalized = np.zeros(len(expected_matrix))
while i < len(expected_matrix):
    expected_matrix_normalized[i] = 2 * ((expected_matrix[i][0] - min_value) / (max_value - min_value)) - 1
    i += 1

training_set, training_expected, test_set, test_expected, testID = cross_validations(training_matrix, expected_matrix_normalized, 3)
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