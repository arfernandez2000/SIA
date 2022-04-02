import matplotlib.pyplot as plt
import numpy as np

plt.style.use('default')

def draw(x_data: list, y_data: list):
    fig, ax = plt.subplots()

    ax.plot(x_data, y_data, linewidth=2.0)

    len_x, len_y = len(x_data), len(y_data)
    ax.set(xlim=(0, len_x), xticks=np.arange(1, len_x),
        ylim=(0, len_y), yticks=np.arange(1, len_y))

    plt.show()