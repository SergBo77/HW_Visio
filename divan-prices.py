# Импортируем библиотеки
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Открытие страницы для поиска диванов на сайте divan.ru
driver.get('https://www.divan.ru/search?ProductSearch%5Bname%5D=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD&no_cache=1')

# Ожидание загрузки страницы
time.sleep(3)

# Нахождение элементов с ценами диванов
prices = driver.find_elements(By.XPATH, "//span[@class='ui-LD-ZU KIkOH']")

price = []

# Извлечение и обработка цен
for price_element in prices:
    pr = price_element.text
    pr_clear = int(pr.replace('руб.', '').replace(' ', ''))
    price.append(pr_clear)

# Закрытие драйвера
driver.quit()

# Создание DataFrame и сохранение цен в CSV-файл
df = pd.DataFrame(price, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

# Вычисление средней цены и вывод на экран
average_price = round(df['Price'].mean(), 2)
print(f'Средняя цена на диваны: {average_price}')

# Построение гистограммы цен на диваны
plt.hist(price, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.title('Гистограмма цен на диваны')
plt.show()




