from datetime import datetime
import math
import numpy
from scipy.optimize import minimize
import sklearn

values = [[(4.4793, -4.0765, -4.0765), 0], [(-4.1793, -4.9218, 1.7664), 1], [(-3.9429, -0.7689, 4.883), 1]]

def g(x):
    return math.exp(x) / (1 + math.exp(x))

def F(W, w, w0, epsilon):
    sum = 0
    for i in range(0, 2):
        aux = 0
        for j in range(0, 3):
            aux += w[i][j] * epsilon[j]
        aux -= w0[i]
        sum += W[i + 1] * g(aux)
    return g(sum - W[0])


def E(x):
    W = x[0:3]
    w = [x[3:6], x[6:9]]
    w_0 = x[9:11]
    return sum((OUT - F(W, w, w_0, IN)) ** 2 for (IN, OUT) in values)

def print_res(x, time ,method):
        print("Resultado")
        print("Metodo: "+ method)
        print("W = " + str(x[0:3]))
        print("w = "+ str([x[3:6]]) + "\t" + str([x[6:9]]))
        print("w0 = " + str(x[9:11]))
        print("Error = " + str(E(x)))
        print("Tiempo: " + str(time))

def main():
    print("COMIENZO")

    x1 = numpy.zeros(11)
    time1 = datetime.nowd
    res1 = minimize(E, x1, args=(), method='L-BFGS-B', jac=None, bounds=None, tol=None, callback=None, options={'disp': None, 'maxcor': 10, 'ftol': 2.220446049250313e-09, 'gtol': 1e-05, 'eps': 1e-08, 'maxfun': 15000, 'maxiter': 15000, 'iprint': - 1, 'maxls': 20, 'finite_diff_rel_step': None})
    print_res(res1, datetime.now - time1, "Gradiente Descendiente")

    x2 = numpy.zeros(11)
    time2 = datetime.now
    res2 = minimize(E, x2, args=(), method='CG', jac=None, tol=None, callback=None, options={'gtol': 1e-05, 'norm': inf, 'eps': 1.4901161193847656e-08, 'maxiter': None, 'disp': False, 'return_all': False, 'finite_diff_rel_step': None})
    print_res(res2, datetime.now - time2, "Gradiente Conjugado")

    x3 = numpy.zeros(11)
    time3 = datetime.now
    res3 = sklearn.neural_network.MLPClassifier(max_iter=15000)
    print_res(res3, datetime.now - time3, "Adam")
