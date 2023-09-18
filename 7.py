class NumberAnalyzer:
    def __init__(self, n):
        self.n = n
        self.is_odd_digit = lambda num: num % 2 == 1 and int(str(num)[0]) % 2 == 1
        self.digit_sum_divisible_by_3 = lambda num: sum(map(int, str(num))) % 3 == 0

    def analyze_numbers(self):
        result = []
        for i in range(0, self.n + 1):
            if self.is_odd_digit(i) and self.digit_sum_divisible_by_3(i):
                result.append(i)
        return result

    def print_numbers(self, numbers):
        print("Числа, удовлетворяющие условиям:")
        for number in numbers:
            print(number)


n = int(input("Введите значение n: "))
result = NumberAnalyzer(n).analyze_numbers()
NumberAnalyzer(n).print_numbers(result)
