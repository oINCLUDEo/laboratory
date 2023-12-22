# 11.	Формируется матрица F следующим образом: если в С сумма чисел  в нечетных столбцах в области 2 больше,
# чем произведение чисел в четных строках в области 1, то поменять в С симметрично области 2 и 3 местами, иначе Е и В
# поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: (К*A)*А– (K *
# AT). Выводятся по мере формирования А, F и все матричные операции последовательно.

import random


def print_matrix(mat):
    for row in mat:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()


def pastemat(matF, matrix, column_index, row_index):
    a = column_index
    for row in matrix:
        for element in row:
            matF[row_index][column_index] = element
            column_index += 1
        row_index += 1
        column_index = a


def matzero(size):
    return [[0 for i in range(size)] for j in range(size)]


def matrix_input(mat, i1, i2, j1, j2):
    zero_mat = matzero(len(mat) // 2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zero_mat[i - i1][j - j1] = mat[i][j]
    return zero_mat


try:
    K = int(input('Введите число K: '))
    n = int(input('Введите число число N, больше или равное 5: '))
    while n < 5:
        n = int(input('Введите число N, большее или равное 5: '))
except ValueError:
    print('Введенный символ не является числом.')
    exit(0)

matA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]

print('Матрица А изначальная:')
print_matrix(matA)

half_n = n // 2
fix_n = half_n
if n % 2 != 0:
    fix_n += 1

matC = matrix_input(matA, 0, half_n, fix_n, n)
matE = matrix_input(matA, fix_n, n, fix_n, n)
matD = matrix_input(matA, fix_n, n, 0, half_n)
matB = matrix_input(matA, 0, half_n, 0, half_n)

print('Подматрицы матрицы A:')
print('Подматрица B')
print_matrix(matB)
print('Подматрица С')
print_matrix(matC)
print('Подматрица D')
print_matrix(matD)
print('Подматрица E')
print_matrix(matE)

comp, summ = 1, 0
for i in range(len(matC)):
    for j in range(len(matC)):
        if i >= j and i + j + 1 <= half_n:
            if i % 2 != 0:
                comp *= matC[i][j]

print('Произведение чисел в четных строках области 1:', comp)
for i in range(len(matC)):
    for j in range(len(matC)):
        if i <= j and i + j + 1 <= half_n:
            if j % 2 == 0:
                summ += matC[i][j]

print('Сумма чисел в нечетных слолбцах области 2:', summ)

if summ > comp:
    print('Сумма чисел  в нечетных столбцах в области 2 больше, чем произведение чисел в четных строках в области 1')
    print('Начальная подматрциа C:')
    print_matrix(matC)
    for i in range(len(matC)):
        for j in range(len(matC)):
            if i <= j and i + j + 1 <= half_n:
                matC[i][j], matC[j][i] = matC[j][i], matC[i][j]
    print('Получившаяся подматрица С:')
    print_matrix(matC)
else:
    print('Сумма чисел  в нечетных столбцах в области 2 меньше, чем произведение чисел в четных строках в области 1')
    matrix_E, matrix_B = matB, matE

matF = matA.copy()
pastemat(matF, matB, 0, 0)
pastemat(matF, matC, fix_n, 0)
pastemat(matF, matD, fix_n, fix_n)
pastemat(matF, matE, 0, fix_n)

print('Матрица F:')
print_matrix(matF)

matFt = matzero(n)

print("Матрица F транспонированая:")
for i in range(n):
    for j in range(n):
        matFt[i][j] = matF[j][i]
print_matrix(matFt)

print('Вычисляем A * F + K * F T:')

matAF = matzero(n)
matTF = matFt.copy()
for i in range(n):
    for j in range(n):
        for k in range(n):
            matAF[i][j] += matA[i][k] * matF[k][j]
print('Результат A * F:')
print_matrix(matAF)

for i in range(n):
    for j in range(n):
        matTF[i][j] *= K

print('Результат K * F:')
print_matrix(matTF)
matres = matzero(n)
for i in range(n):
    for j in range(n):
        matres[i][j] = matAF[i][j] + matTF[i][j]
print('Результат:')
print_matrix(matres)
