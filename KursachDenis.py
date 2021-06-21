import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def calculate_slope(x, y):
    mx = x - x.mean()
    my = y - y.mean()
    return sum(mx * my) / sum(mx**2)


def get_params(x, y):
    a = calculate_slope(x, y)
    b = y.mean() - a * x.mean()
    return a, b


def line(xarr, yarr):
    a, b = get_params(xarr, yarr)
    lin_reg = a * xarr + b
    plt.xlabel('Координата X')
    plt.ylabel('Координата Y')
    plt.plot(xarr, yarr)
    plt.scatter(xarr, yarr)
    plt.plot(xarr, lin_reg, color='red')
    plt.show()


def normal(x, y):
    fig, ax = plt.subplots()
    plt.xlabel('Координата X')
    plt.ylabel('Координата Y')
    ax.plot(x, y)
    plt.show()


plt.style.use('seaborn-whitegrid')
xarr = np.arange(74)
yarr = np.random.randint(0, 90, 74)

with open('newfile.txt', 'w', encoding='utf-8') as f:
    for i in range(74):
        f.write(f'x = {xarr[i]}, y = {yarr[i]} \n')

normal(xarr, yarr)
line(xarr, yarr)
