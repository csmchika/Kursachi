import matplotlib.pyplot as plt
import numpy as np
from statistics import mean


class Graph:

    def __init__(self):
        self.xarr = np.random.randint(-100, 100, 72)
        self.yarr = np.random.uniform(-100, 100, 72)

    def write_txt(self):

        with open('x.txt', 'w', encoding='utf-8') as f:
            for i in range(len(self.xarr)):
                f.write(f'{self.xarr[i]},')

        with open('y.txt', 'w', encoding='utf-8') as f:
            for i in range(len(self.yarr)):
                f.write(f'{self.yarr[i]},')

    def draw_graph(self):

        with open('x.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.x = line.split(',')
                self.x = self.x[:-1]
            for i in range(len(self.x)):
                self.x[i] = int(self.x[i])

        with open('y.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.y = line.split(',')
                self.y = self.y[:-1]
            for i in range(len(self.y)):
                self.y[i] = float(self.y[i])
        self.fig, self.ax = plt.subplots()
        plt.xlabel('Координата X')
        plt.ylabel('Координата Y')
        plt.plot(self.x, self.y)
        plt.scatter(self.x, self.y)
        plt.show()

    def count_deviation(self):
        self.xmax = 0
        self.xmin = 1000
        self.ymax = 0
        self.ymin = 1000
        self.xmean = mean(self.x)
        self.ymean = mean(self.y)

        for i in range(len(self.x)):
            if abs(self.x[i] - self.xmean) > self.xmax:
                self.xmax = abs(self.x[i] - self.xmean)
            elif abs(self.x[i] - self.xmean) < self.xmin:
                self.xmin = abs(self.x[i] - self.xmean)

        for i in range(len(self.y)):
            if abs(self.y[i] - self.ymean) > self.ymax:
                self.ymax = abs(self.y[i] - self.ymean)
            elif abs(self.y[i] - self.ymean) < self.ymin:
                self.ymin = abs(self.y[i] - self.ymean)

        self.xy = self.x + self.y
        self.xymean = mean(self.xy)

        with open('xy.txt', 'w', encoding='utf-8') as f:
            f.write(f'Минимальное отклонение x от среднего - {self.xmin}, Максимальное отклонение x от среднего - {self.xmax} \n')
            f.write(f'Минимальное отклонение y от среднего - {self.ymin}, Максимальное отклонение y от среднего - {self.ymax} \n')
            f.write(f'Среднее значение всех x и y - {self.xymean}')


graph1 = Graph()
graph1.write_txt()
graph1.draw_graph()
graph1.count_deviation()
graph2 = Graph()
graph2.write_txt()
graph2.draw_graph()
graph2.count_deviation()
