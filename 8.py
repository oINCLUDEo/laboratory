# Вариант 11. Вывести все натуральные числа до n, которые начинаются и заканчиваются нечетной цифрой.
# Усложнение: Число также должно делиться на 3
import tkinter as tk
from tkinter import messagebox


class NumberAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализ чисел")

        self.label = tk.Label(root, text="Введите значение n:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.analyze_button = tk.Button(root, text="Анализ", command=self.analyze)
        self.analyze_button.pack()

        self.result_text = tk.Text(root, height=10, width=30)
        self.result_text.pack()

    def analyze(self):
        n = self.entry.get()
        if not n.isdigit():
            messagebox.showerror(title="Ошибка",
                                message="Вы ввели некорректное число")
        elif int(n) < 3:
            messagebox.showerror(title="Ошибка",
                                 message="Нет подходящих чисел до " + n)
        else:
            n = int(n)
            analyzer = Numbers(n)
            result = analyzer.analyze_numbers()

            self.result_text.delete(0.0, tk.END)
            for number in result:
                self.result_text.insert(0.0, f"{number}\n")


class Numbers:
    def __init__(self, n):
        self.n = n
        self.nechet = lambda num: num % 2 == 1 and int(str(num)[0]) % 2 == 1
        self.divisible_3 = lambda num: sum(map(int, str(num))) % 3 == 0

    def analyze_numbers(self):
        result = []
        for i in range(1, self.n + 1):
            if self.nechet(i) and self.divisible_3(i):
                result.append(i)
        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberAnalyzerGUI(root)
    root.mainloop()
