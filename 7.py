class Numbers:
    def __init__(self, n):
        self.n = n
        self.nechet = lambda num: num % 2 == 1 and int(str(num)[0]) % 2 == 1
        self.divisible_3 = lambda num: num % 3 == 0

    def analyze_numbers(self):
        result = []
        for i in range(0, self.n + 1):
            if self.nechet(i) and self.divisible_3(i):
                result.append(i)
        return result

    def print_numbers(self, numbers):
        print("Числа, удовлетворяющие условиям:")
        for number in numbers:
            print(number)


n = int(input("Введите значение n: "))
result = Numbers(n).analyze_numbers()
Numbers(n).print_numbers(result)
