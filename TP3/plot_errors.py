import matplotlib.pyplot as plt
import numpy as np

errors = []

def add_error(e):
    errors.append(e)

def plot():
    plt.style.use('default')
    fig, ax = plt.subplots()
    length = len(errors)
    y_max = np.amax(errors)
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    x = np.arange(0, length)
    ax.set(xlim=(0,length), xticks=np.arange(0,length, length/10),
            ylim=(0,y_max + 1), yticks=np.arange(0,y_max + 1, y_max/10))
    ax.plot(x,errors)
    plt.show()

def plot_list_error(errs, title=''):
    plt.style.use('default')
    fig, ax = plt.subplots()
    length = len(errs)
    y_max = np.amax(errs)
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.title(title)
    x = np.arange(0, length)
    ax.set(xlim=(0,length), xticks=np.arange(0,length, length/10),
            ylim=(0,y_max + 1), yticks=np.arange(0,y_max + 1, y_max/10))
    ax.plot(x,errs)
    plt.show()
