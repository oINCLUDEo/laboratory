# 11.	Определить количество пассажиров на борту в возрастном интервале мода +- 10 позиций и сколько из них выжило
import csv

# Открываем файл titanic.csv
with open('titanic.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Читаем файл как словарь
    # Создаем пустые списки для хранения возрастов и выживших пассажиров
    ages = []
    survived = []

    # Читаем каждую строку из файла
    for row in reader:
        age = row['Age']
        if age != '':  # Проверяем, что возраст указан
            ages.append(float(age))  # Добавляем возраст в список

            # Проверяем, выжил ли пассажир
            if row['Survived'] == '1':
                survived.append(float(age))  # Добавляем возраст выжившего пассажира в список

# Вычисляем моду и диапазон возрастов для поиска пассажиров
age_mode = max(set(ages), key=ages.count)
lower_limit = age_mode - 10  # Нижний диапазон
upper_limit = age_mode + 10  # Верхний диапозон

# Считаем количество пассажиров в указанном возрастном интервале и количество выживших среди них
passengers_in_range = sum(1 for age in ages if lower_limit <= age <= upper_limit)
survived_in_range = sum(1 for age in survived if lower_limit <= age <= upper_limit)

print(f"Мода Возраста: {age_mode}")
print(f"Количество пассажиров в возрастном интервале от {lower_limit} до {upper_limit}: {passengers_in_range}")
print(f"Из них выжило: {survived_in_range}")
