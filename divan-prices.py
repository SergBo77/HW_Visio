from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

driver = webdriver.Chrome()

driver.get('https://www.divan.ru/search?ProductSearch%5Bname%5D=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD&no_cache=1')

time.sleep(3)

prices = driver.find_elements(By.XPATH,"//span[@class='ui-LD-ZU KIkOH']")

price = []

for price_element in prices:
    pr = price_element.text
    pr_clear = int(pr.replace('руб.', '').replace(' ', ''))
    price.append(pr_clear)

driver.quit()

df = pd.DataFrame(price, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

average_price = round(df['Price'].mean(), 2)
print(f'Средняя цена на диваны: {average_price}')

plt.hist(price, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.title('Гистограмма цен на диваны')
plt.show()




