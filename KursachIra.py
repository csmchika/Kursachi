import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def graph_max():
    global maxi
    plt.xlabel('Координата X')
    plt.ylabel('Координата Y')
    plt.plot(df1['x'], df1['y'])
    for i in range(len(df1['noun'])):
        if df1.iloc[i]['noun'] == maxi:
            plt.scatter(df1.iloc[i]['x'], df1.iloc[i]['y'], label='Точка наивысшего попадания')
    plt.legend(shadow=False, fontsize=8, loc='lower left')
    plt.show()


plt.style.use('seaborn-whitegrid')
xarr_10 = np.arange(1, 11)
xarr = np.random.randint(1, 11, 70)
yarr = np.random.randint(1, 11, 70)
diction = {}
df = pd.DataFrame({
    'x': xarr,
    'y': yarr,
    'noun': np.nan
})
t = 0
df1 = pd.DataFrame(columns=['x', 'y', 'noun'])
df2 = pd.DataFrame(columns=['x', 'y'])
df3 = pd.DataFrame(columns=['x', 'y'])
for x in xarr_10:
    diction = {}
    for k in xarr_10:
        diction[k] = 0
    for i in range(len(xarr)):
        if df.iloc[i]['x'] == x:
            diction[df.iloc[i]['y']] += 1
    for key, value in diction.items():
        if diction[key] != 0:
            df1 = df1.append({'x': x, 'y': key, 'noun': value}, ignore_index=True)
for i in range(len(df1['noun'])):
    if df1.iloc[i]['noun'] > 1:
        df2 = df2.append({'x': df1.iloc[i]['x'], 'y': df1.iloc[i]['y']}, ignore_index=True)
    if df1.iloc[i]['noun'] > 3:
        df3 = df3.append({'x': df1.iloc[i]['x'], 'y': df1.iloc[i]['y']}, ignore_index=True)
maxi = max(df1['noun'])
with open('Kursovaya.txt', 'w', encoding='utf-8') as f:
    for i in range(len(xarr)):
        f.write(f'x - {xarr[i]}, y - {yarr[i]} \n')
    f.write(f'А теперь координаты с наибольшим попаданием: \n')
    for i in range(len(df1['noun'])):
        if df1.iloc[i]['noun'] == maxi:
            f.write(f'x - {df1.iloc[i]["x"]}, y - {df1.iloc[i]["y"]}, количество попаданий - {maxi}\n')

fig, ax = plt.subplots()
plt.xlabel('Координата X')
plt.ylabel('Координата Y')
plt.scatter(df1['x'], df1['y'], label='1')
plt.scatter(df2['x'], df2['y'], label='2 - 3')
plt.scatter(df3['x'], df3['y'], label='> 3')
plt.legend(shadow=False, fontsize=8, loc='lower left')
plt.show()
graph_max()
