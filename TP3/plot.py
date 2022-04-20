import matplotlib.pyplot as plt
import numpy as np
from config_loader import trainData as train, expectOut as goal

plt.style.use('default')

def plot(w, wait=False):
    fig, ax = plt.subplots()
    w0, w = w[-1], w[:-1]
    x = [-1,1]
    print(w)
    w = np.flip(w)
    print(w)
    w = -w*x-w0 #No se porque pero con + no anda bien
    for i in range(len(train)):
        color = "black"
        if goal[i] == 1:
            color = "red"
        p = train[i]
        ax.plot(p[0],p[1], marker="o", markersize= 5, markeredgecolor=color, markerfacecolor=color)
    ax.grid()
    ax.plot(x,w)
    ax.set(xlim=(-2,2), xticks=np.arange(-2,2+1),
        ylim=(-2,2), yticks=np.arange(-2,2+1))
    if wait:
        plt.show()
    else:
        plt.show(block=False)
        plt.pause(1)
        plt.close()