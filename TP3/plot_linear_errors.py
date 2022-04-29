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
    x = np.arange(0, length)
    ax.set(xlim=(0,length), xticks=np.arange(0,length, length/10),
            ylim=(0,y_max + 1), yticks=np.arange(0,y_max + 1, y_max/10))
    ax.plot(x,errors)
    print(errors)
    plt.show()