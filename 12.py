# 11. Вычислить сумму знакопеременного ряда (|х(3n)|)/(3n)!, где х-матрица ранга к (к и матрица задаются случайным
# образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков
# после запятой. У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого  +.

import random as ran
import numpy as np
import decimal as de

# region Создание матрицы
k = ran.randint(1, 10)
x = np.random.uniform(-1, 1, (k, k))
# endregion

t = input("Введите число t > 0: ")
# region Проверка ввода t
while True:
    if t.isdigit() == True and 1 < int(t) <= 100:
        t = int(t)
        break
    elif not t.isdigit():
        t = input("t не является числом, введите его ещё раз: ")
    elif int(t) < 1 or int(t) > 100:
        t = input("Число t меньше единицы или больше ста, введите его ещё раз: ")
# endregion

n = 1  # Номер слагаемого
n3_factotial = 3  # Факториал
result = de.Decimal(0)  # Результат
de.getcontext().prec = t + 60  # установка точности
# region Вычисление слагаемого до точности с t
while abs(result.as_tuple().exponent) < t:
    result += de.Decimal(np.linalg.det(x ** (3 * n))) * de.Decimal(1 / n3_factotial)  # вычисление слагаемого/результата
    n += 1  # Номер слагаемого увеличился
    n3_factotial *= n  # Обновление факториала
# endregion
# region Вывод
print('Матрица X:\n', x)
print(f"Ответ: {result:.{t}f}")
# endregion
