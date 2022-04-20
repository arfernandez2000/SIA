import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

def plot(w,train,goal):
    # plot
    fig, ax = plt.subplots()
    w0, w = w[-1], w[:-1]
    x = [-1,1]
    w = -w*x - w0
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

    plt.show()