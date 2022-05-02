import numpy as np
import random
from perceptrons.Perceptron import Perceptron

class NonLinearSimplePerceptron():

    def __init__(self, input_size, activation_function, der_activation_function, eta=0.001, delta=0.0049, iterations_qty=1000):
        self.eta = eta
        self.eta = eta
        self.activation_function = activation_function
        self.weights = np.array(np.random.rand(input_size + 1))
        self.der_activation_function = der_activation_function
        self.delta = delta
        self.iterations_qty = iterations_qty

    def predict_with(self, a_input):
        dot_product = self.weights.T.dot(a_input)
        return self.activation_function(dot_product)

    def predict(self, a_input):
        return self.predict_with(np.insert(a_input, 0, 1))

    def error(self, training_set, expected_set):
        sum = 0
        for i in range(len(training_set)):
            x = training_set[i]
            y = expected_set[i]
            predicted = self.predict(x)
            aux = (predicted - y) ** 2
            sum += aux
        return sum / 2

    def accuracies(self, test_set, expected_set):
        j = 0
        test_correct_cases = 0
        while j < len(test_set):
            error = expected_set[j] - self.predict(test_set[j])
            if error < self.delta:
                test_correct_cases += 1
            j += 1

        return test_correct_cases/len(test_set)

    def train(self, training_set, expected_set, test_set, test_expected_test, error_epsilon=0, print_data=False):
        errors = []
        epochs = []
        training_accuracies = []
        training_set = np.array(training_set)
        expected_set = np.array(expected_set)
        ii = 0
        shuffled_list = [a for a in range(0, len(training_set))]
        random.shuffle(shuffled_list)
        p = len(training_set)
        err = 1
        min_error = 2 * p
        error = 0
        test_accuracies = []
        while ii < self.iterations_qty and err > error_epsilon:
            j = 0
            training_correct_cases = 0
            while j < len(shuffled_list):
                biased_input = np.insert(training_set[shuffled_list[j]], 0, 1)
                predicted_value = self.predict_with(biased_input)
                error = expected_set[shuffled_list[j]] - predicted_value
                if error < self.delta:
                    training_correct_cases += 1
                self.weights = self.weights + (self.eta * error * self.der_activation_function(
                    self.weights.T.dot(biased_input)) * biased_input.T)
                j += 1

            err = self.error(training_set, expected_set)
            if err < min_error:
                min_error = err
            errors.append(err)
            print("ERROR", err)
            training_accuracies.append(training_correct_cases / len(training_set))
            print("Epoch: ", ii)
            print("min error", min_error)
            print("weights: ", self.weights)

            error = self.error(test_set, test_expected_test)
            test_accuracies.append(self.error(test_set, test_expected_test))
            epochs.append(ii)
            ii += 1
        return min_error, epochs, errors, training_accuracies, error, test_accuracies

    def test(self, test_set, expected_test):
        error = self.error(test_set, expected_test)
        accuracies = self.accuracies(test_set, expected_test)
        return error, accuracies
