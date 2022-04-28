import matplotlib.pyplot as plt
import numpy as np

errors = []

def add_error(e):
    errors.append(e)

def plot():
    plt.style.use('default')
    fig, ax = plt.subplots()
    length = len(errors)
    x = np.arange(0, length)
    ax.set(xlim=(0,length), xticks=np.arange(0,length),
            ylim=(0,length), yticks=np.arange(0,length))
    ax.plot(x,errors)
    print(errors)
    plt.show()