from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

#No testeado
def plot_predictions(predictions):
    plt.style.use('default')
    fig, ax = plt.subplots()
    y_max = 100
    x = np.arange(0,len(predictions))
    length = len(x)
    ax.set(xlim=(0,length), xticks=np.arange(0,length),
            ylim=(0,y_max), yticks=np.arange(0,y_max, 10))
    ax.plot(x,predictions)
    #plt.legend()
    plt.show(block=False)