import matplotlib.pyplot as plt
import numpy as np
from config_loader import trainDataEx1 as train, expectOutEx1 as goal

plt.style.use('default')
ws = []
x = np.linspace(-2,2,100)
points = list(map(lambda p: p[:-1], train))
fig, ax = plt.subplots()

def set_ax():
    for i in range(len(points)):
        color = "black"
        if goal[i] == 1:
            color = "red"
        p = points[i]
        ax.plot(p[0],p[1], marker="o", markersize= 5, markeredgecolor=color, markerfacecolor=color)
    ax.grid()
    ax.set(xlim=(-2,2), xticks=np.arange(-2,2),
            ylim=(-2,2), yticks=np.arange(-2,2))

def add_w(w):
    set_ax()
    w = (w[1] * x + w[2]) / -w[0]
    ws.append(w)
    ax.plot(x,w)
    plt.show(block=False)
    plt.pause(0.5)
    ax.cla()

def plot():
    set_ax()
    ax.plot(x,ws[-1])
    plt.show()