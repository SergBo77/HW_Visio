import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=20)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Гистограмма нормального распределения")
plt.show()


x = np.random.rand(20)
y = np.random.rand(20)

plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния")
plt.show()