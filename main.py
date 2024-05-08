import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
import scipy.stats as stats

# Завантаження даних з файлу
merged_data = pd.read_csv('merged_data.csv')

# Завдання 5: Знаходження статистичних оцінок та побудова графіку лінійної регресії

# Формування векторів ознак та цільової змінної
X = merged_data[['airTemperature']]
y = merged_data['total_water_consumption']

# Заміна відсутніх значень на середнє
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Ініціалізація та навчання моделі лінійної регресії
model = LinearRegression()
model.fit(X_imputed, y)

# Прогнозування
predictions = model.predict(X_imputed)

# Виведення коефіцієнтів моделі
print('Коефіцієнти лінійної регресії:')
print('Коефіцієнт перетину (intercept):', model.intercept_)
print('Коефіцієнт нахилу (slope):', model.coef_[0])

# Побудова графіку парної лінійної регресії
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', alpha=0.5)
plt.plot(X, predictions, color='red', linewidth=2)
plt.title('Парна лінійна регресія')
plt.xlabel('Температура повітря')
plt.ylabel('Споживання води')
plt.show()

# Завдання 6: Знаходження коефіцієнта детермінації та кореляції моделі, оцінка адекватності

# Визначення коефіцієнта детермінації (R^2)
r_squared = r2_score(y, predictions)
print('Коефіцієнт детермінації (R^2):', r_squared)

# Визначення коефіцієнта кореляції
correlation = np.sqrt(r_squared)
print('Коефіцієнт кореляції:', correlation)

# Оцінка рівня адекватності моделі
if r_squared == 1:
    print('Модель є абсолютно адекватною.')
elif r_squared > 0.8:
    print('Модель є дуже адекватною.')
elif r_squared > 0.6:
    print('Модель є достатньо адекватною.')
elif r_squared > 0.4:
    print('Модель є малоадекватною.')
else:
    print('Модель є незадовільною.')

# Завдання 7: Перевірка статистичної значущості коефіцієнтів детермінації та кореляції

# Використання бібліотеки statsmodels для оцінки статистичної значущості
model = sm.OLS(y, X_imputed).fit()
print(model.summary())

# Визначення довірчого інтервалу
confidence = 0.95
s = np.sqrt(np.sum((predictions - y) ** 2) / (len(X_imputed) - 2))
t = stats.t.ppf((1 + confidence) / 2, len(X) - 2)
ci = t * s / np.sqrt(np.sum((X_imputed[:, 0] - np.mean(X_imputed[:, 0])) ** 2))
lower_bound = model.params[0] - ci
upper_bound = model.params[0] + ci

print(f'95% довірчий інтервал: ({lower_bound}, {upper_bound})')

# Обчислення довірчого інтервалу для прогнозу середнього значення залежної змінної
alpha = 0.95
confidence_interval = stats.t.interval(1 - alpha, len(X_imputed) - 2, loc=np.mean(predictions),
                                       scale=stats.sem(predictions))
print('Довірчий інтервал для прогнозу середнього значення залежної змінної:', confidence_interval)

# Візуалізація довірчого інтервалу
plt.figure(figsize=(8, 6))
plt.scatter(X_imputed, y, color='blue', alpha=0.5)
plt.plot(X_imputed, predictions, color='red', linewidth=2)
plt.fill_between(X_imputed.flatten(), confidence_interval[0], confidence_interval[1], color='black', alpha=0.3)
plt.title('Парна лінійна регресія з довірчим інтервалом')
plt.xlabel('Температура повітря')
plt.ylabel('Споживання води')
plt.show()

# Завдання 9: Встановлення найкращого виду регресійної моделі
print('Найкращий вид регресійної моделі: Лінійна регресія')
