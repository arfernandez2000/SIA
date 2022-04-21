import matplotlib.pyplot as plt
import numpy as np
from config_loader import trainData as train, expectOut as goal

plt.style.use('default')
ws = []
points = []
x_mult = [-1,1]
x_point = [0,1]
for t in train:
        aux = []
        for i in t:
            if i == -1:
                aux.append(0) #Usa -1 para los calculos pero para graficar entre 0 y 1 lo acomoda aca, NO ES NECESARIO
            else: 
                aux.append(i)
        points.append(aux)

fig, ax = plt.subplots()
def set_ax():
    for i in range(len(points)):
        color = "black"
        if goal[i] == 1:
            color = "red"
        p = points[i]
        ax.plot(p[0],p[1], marker="o", markersize= 5, markeredgecolor=color, markerfacecolor=color)
    ax.grid()
    ax.set(xlim=(-1,2), xticks=np.arange(-1,2),
            ylim=(-1,2), yticks=np.arange(-1,2))

def add_w(w):
    set_ax()
    w0, w = w[-1], w[:-1]
    w = -w*x_mult-w0
    #w = w*x_mult-w0
    w = w+1 #SIN ESTO NO ANDA, lo agregue porque los calculos se realizan con 3 entradas pero graficamos solo 2
    ws.append(w)
    ax.plot(x_point,w)
    plt.show(block=False)
    plt.pause(0.5)
    ax.cla()

def plot():
    set_ax()
    ax.plot(x_point,ws[-1])
    plt.show()