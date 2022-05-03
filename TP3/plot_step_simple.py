import matplotlib.pyplot as plt
import numpy as np
from config_loader import trainData as train, expectOut as goal, perceptron

def set_ax(points,ax,plt):
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    for i in range(len(points)):
        color = "black"
        if goal[i] == 1:
            color = "red"
        p = points[i]
        ax.plot(p[0],p[1], marker="o", markersize= 5, markeredgecolor=color, markerfacecolor=color)
    ax.grid()
    ax.set(xlim=(-2,2), xticks=np.arange(-2,2),
            ylim=(-2,2), yticks=np.arange(-2,2))
def plot(ws):
    plt.style.use('default')
    #ws = []
    x = np.linspace(-2,2,5)
    points = list(map(lambda p: p[:-1], train))
    fig, ax = plt.subplots()
    for i in range(0,len(ws)):
        set_ax(points,ax,plt)
        w = ws[i]
        print('///////// w: ', w)
        w = (w[1] * x + w[2]) / -w[0]
        ax.plot(x,w)
        plt.show(block=False)
        plt.pause(0.5)
        #plt.close()
        ax.cla()
        ws[i] = w
    set_ax(points,ax,plt)
    print(x,ws[-1])
    ax.plot(x,ws[-1])
    plt.show()