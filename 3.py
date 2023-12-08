import numpy as np


def main():
    # Вводим два числа K и P
    K = int(input("Введите K: "))
    P = int(input("Введите P: "))

    # Создаем матрицу A
    N = 2 * P
    A = np.random.randint(-10, 10, (N, N))

    # Заполняем матрицы B, C, D, E
    B = A[:N // 2, :N // 2]
    C = A[:N // 2, N // 2:]
    D = A[N // 2:, :N // 2]
    E = A[N // 2:, N // 2:]

    # Формируем матрицу F
    if np.sum(C[1::2, 0::2]) > np.prod(B[0::2, 0::2]):
        F = np.array([[C[0::2, 0::2], C[1::2, 0::2]], [C[0::2, 1::2], C[1::2, 1::2]]])
    else:
        F = np.array([[E[0::2, 0::2], B[0::2, 0::2]], [E[0::2, 1::2], B[0::2, 1::2]]])

    # Вычисляем выражение (K * A) * A - (K * АТ)
    result = np.matmul(K * A, A) - np.matmul(K * A.T, A.T)

    # Выводим матрицы A, E и все матричные операции
    print("Матрица A:")
    print(A)
    print("Матрица E:")
    print(E)
    print("Матрица F:")
    print(F)
    print("Выражение (K * A) * A - (K * АТ):")
    print(result)


if __name__ == "__main__":
    main()
