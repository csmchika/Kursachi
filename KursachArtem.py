import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-whitegrid')
xarr = np.arange(70)
yarr = np.random.randint(0, 100, 70)

with open('Kursovaya_5.txt', 'w', encoding='utf-8') as f:
    for i in range(len(xarr)):
        f.write(f'x - {xarr[i]}, y - {yarr[i]} \n')

_yarr = np.arange(100)
xarr1 = []
xarr2 = []
xarr3 = []
xarr4 = []
for i in range(100):
    xarr1.append(14)
    xarr2.append(28)
    xarr3.append(42)
    xarr4.append(56)
max1 = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0
minx1 = 100
minx2 = 100
minx3 = 100
minx4 = 100
minx5 = 100
for x in range(len(xarr)):
    if x < 14:
        if yarr[x] > max1:
            max1 = yarr[x]
        elif yarr[x] < minx1:
            minx1 = yarr[x]
    elif x < 28:
        if yarr[x] > max2:
            max2 = yarr[x]
        elif yarr[x] < minx2:
            minx2 = yarr[x]
    elif x < 42:
        if yarr[x] > max3:
            max3 = yarr[x]
        elif yarr[x] < minx3:
            minx3 = yarr[x]
    elif x < 56:
        if yarr[x] > max4:
            max4 = yarr[x]
        elif yarr[x] < minx4:
            minx4 = yarr[x]
    else:
        if yarr[x] > max5:
            max5 = yarr[x]
        elif yarr[x] < minx5:
            minx5 = yarr[x]

plt.xlabel('Координата X')
plt.ylabel('Координата Y')
plt.plot(xarr, yarr)
plt.scatter(xarr, yarr)
plt.plot(xarr1, _yarr)
plt.plot(xarr2, _yarr)
plt.plot(xarr3, _yarr)
plt.plot(xarr4, _yarr)
print(f'Максимальное значение в 1 секции - {max1}, минимальное значение в 1 секции - {minx1}, разность - {max1 - minx1}')
print(f'Максимальное значение в 2 секции - {max2}, минимальное значение в 2 секции - {minx2}, разность - {max2 - minx2}')
print(f'Максимальное значение в 3 секции - {max3}, минимальное значение в 3 секции - {minx3}, разность - {max3 - minx3}')
print(f'Максимальное значение в 4 секции - {max4}, минимальное значение в 4 секции - {minx4}, разность - {max4 - minx4}')
print(f'Максимальное значение в 5 секции - {max5}, минимальное значение в 5 секции - {minx5}, разность - {max5 - minx5}')
plt.show()




