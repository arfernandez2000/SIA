import numpy as np
from perceptrons.NonLinearSimplePerceptron import *
from utils import *
from config_loader import *
from utils import *
from config_utils import parse_data

training_matrix = parse_data('./entries_2.txt')
expected_matrix = parse_data('./expected_output_2.txt')
print("PARSEO DATA")

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
min_err, epochs, error_list, training_accuracies, min_err_test, test_accuracies = perceptron_nolineal2.train(training_set, training_expected, test_set, test_expected)
min_err_test, test_accuracies = perceptron_nolineal2.test(test_set, test_expected)

print()
print("training error", min_err)
print("testing error", min_err_test)
print()

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