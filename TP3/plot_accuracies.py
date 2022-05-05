from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

#No testeado
def plot_acc(epochs, training, test):
    plt.style.use('default')
    fig, ax = plt.subplots()
    y_max = np.amax(np.array([np.amax(training),np.amax(test)]))
    plt.ylabel('Accuracie')
    plt.xlabel('Epochs')
    length = len(epochs)
    ax.set(xlim=(0,length), xticks=np.arange(0,length, length/10),
            ylim=(0,y_max + 1), yticks=np.arange(0,y_max + 1, y_max/10))
    ax.plot(epochs,training, label='Training')
    ax.plot(epochs,test, label='Test')
    plt.legend()
    plt.show(block=True)