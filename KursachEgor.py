import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-whitegrid')
xarr = np.arange(75)
yarr = np.random.randint(0, 100, 75)
ymean = yarr.mean()
ymeanarr = []
for i in range(75):
    ymeanarr.append(ymean)
ymin = yarr.min()
ymax = yarr.max()
xmin, xmax = 0, 0
diction = {}

for x in range(75):
    diction[f'{xarr[x]}'] = f'{yarr[x]}'

for key, value in diction.items():
    if int(value) == int(ymin):
        xmin = int(key)
    elif int(value) == int(ymax):
        xmax = int(key)

with open('file_kursach.txt', 'w', encoding='utf-8') as f:
    for i in range(75):
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
