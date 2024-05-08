import pandas as pd
import matplotlib.pyplot as plt

# Завантажимо дані з файлу
merged_data = pd.read_csv('merged_data.csv')

# Виведемо графіки
plt.figure(figsize=(15, 12))

# Температура повітря
plt.subplot(2, 3, 1)
plt.scatter(merged_data['airTemperature'], merged_data['total_water_consumption'], alpha=0.5)
plt.title('Температура повітря vs Споживання води')
plt.xlabel('Температура повітря')
plt.ylabel('Споживання води')

# Температура точки роси
plt.subplot(2, 3, 2)
plt.scatter(merged_data['dewTemperature'], merged_data['total_water_consumption'], alpha=0.5)
plt.title('Температура точки роси vs Споживання води')
plt.xlabel('Температура точки роси')
plt.ylabel('Споживання води')

# Глибина опадів за 1 годину
plt.subplot(2, 3, 3)
plt.scatter(merged_data['precipDepth1HR'], merged_data['total_water_consumption'], alpha=0.5)
plt.title('Глибина опадів за 1 годину vs Споживання води')
plt.xlabel('Глибина опадів за 1 годину')
plt.ylabel('Споживання води')

# Глибина опадів за 6 годин
plt.subplot(2, 3, 4)
plt.scatter(merged_data['precipDepth6HR'], merged_data['total_water_consumption'], alpha=0.5)
plt.title('Глибина опадів за 6 годин vs Споживання води')
plt.xlabel('Глибина опадів за 6 годин')
plt.ylabel('Споживання води')

# Швидкість вітру
plt.subplot(2, 3, 5)
plt.scatter(merged_data['windSpeed'], merged_data['total_water_consumption'], alpha=0.5)
plt.title('Швидкість вітру vs Споживання води')
plt.xlabel('Швидкість вітру')
plt.ylabel('Споживання води')

plt.tight_layout()
plt.show()
