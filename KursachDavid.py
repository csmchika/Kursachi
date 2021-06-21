import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-whitegrid')
xarr = np.arange(72)
yarr = np.random.uniform(0, 100, 72)
ymean = yarr.mean()
ymeanarr = []
for i in range(len(xarr)):
    ymeanarr.append(ymean)
ymin = yarr.min()
ymax = yarr.max()
xmin, xmax = 0, 0
diction = {}

for x in range(len(xarr)):
    diction[float(f'{xarr[x]}')] = float(f'{yarr[x]}')

for key, value in diction.items():
    if value == ymin:
        xmin = key
    elif value == ymax:
        xmax = key

with open('Kursovaya_3_file.txt', 'w', encoding='utf-8') as f:
    for i in range(len(xarr)):
        f.write(f'x - {xarr[i]}, y - {yarr[i]} \n')

fig, ax = plt.subplots()
plt.xlabel('Координата X')
plt.ylabel('Координата Y')
plt.plot(xarr, yarr)
plt.scatter(xarr, yarr)
plt.scatter(xmin, ymin, label='Минимальное значение')
plt.scatter(xmax, ymax, label='Максимальное значение')
plt.plot(xarr, ymeanarr, color='red', label='Среднее значение')
plt.legend(shadow=False, fontsize=8, loc='lower left')
plt.show()
