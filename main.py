# Импортируем библиотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Генерация случайных данных с нормальным распределением
data = np.random.normal(0, 1, 1000)

# Построение гистограммы нормального распределения
plt.hist(data, bins=20)
plt.xlabel("x ось")  # Название оси x
plt.ylabel("y ось")  # Название оси y
plt.title("Гистограмма нормального распределения")  # Заголовок графика
plt.show()  # Отображение графика

# Генерация случайных данных для диаграммы рассеяния
x = np.random.rand(20)
y = np.random.rand(20)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.xlabel("ось Х")  # Название оси X
plt.ylabel("ось Y")  # Название оси Y
plt.title("Диаграмма рассеяния")  # Заголовок графика
plt.show()  # Отображение графика