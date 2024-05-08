import pandas as pd

# Завантажимо дані з файлів
water_data = pd.read_csv('datasets/water_cleaned.csv')
weather_data = pd.read_csv('datasets/weather.csv')

# Оберемо необхідні колонки з даних про погоду
selected_weather_data = weather_data[weather_data['site_id'] == 'Panther'][['timestamp',
                                                                            'airTemperature',
                                                                            'dewTemperature',
                                                                            'precipDepth1HR',
                                                                            'precipDepth6HR',
                                                                            'windSpeed']]

# Виберемо тільки ті дані з датасету погоди, для яких є відповідні дані про споживання води
selected_weather_data = selected_weather_data[selected_weather_data['timestamp'].isin(water_data['timestamp'])]

# Сумуємо дані про споживання води за будівлі з site_id = Panther
water_data['total_water_consumption'] = (water_data[[col for col in water_data.columns if 'Panther' in col]]
                                         .sum(axis=1, skipna=True, numeric_only=True))

# Видалимо колонки з даними про споживання води за окремі будівлі
water_data.drop(columns=[col for col in water_data.columns if 'Panther' in col or 'Bobcat' in col or 'Wolf' in col],
                inplace=True)

# Об'єднаємо дані про воду та погоду за допомогою стовпця timestamp
merged_data = pd.merge(water_data, selected_weather_data, on='timestamp', how='inner')

# Збережемо об'єднані дані в новий CSV файл
merged_data.to_csv('merged_data.csv', index=False)
