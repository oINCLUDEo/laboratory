import random as ran
import numpy as np
import decimal as de

k = ran.randint(1, 10)
x = np.random.uniform(-1, 1, (k, k))

t = input("Введите число t > 0: ")
while True:
    if t.isdigit() == True and 1 < int(t) <= 100:
        t = int(t)
        break
    elif not t.isdigit():
        t = input("t не является числом, введите его ещё раз: ")
    elif int(t) < 1 or int(t) > 100:
        t = input("Число t меньше единицы или больше ста, введите его ещё раз: ")

n = 1
n3_factotial = 3
result = de.Decimal(0)
de.getcontext().prec = t + 60  # установка точности
count = de.Decimal(0)
while abs(result.as_tuple().exponent) < t:  # цикл while пока число знаков после запятой не будет больше или равно t
    result += de.Decimal(np.linalg.det(x ** (3 * n))) * de.Decimal(1 / n3_factotial)  # вычисление слагаемого
    n += 1
    n3_factotial *= n

print('Матрица X:\n', x)  # вывод матрицы
print(f"Ответ: {result:.{t}f}")
