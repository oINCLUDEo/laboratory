import tkinter as tk


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
        n = int(self.entry.get())
        analyzer = NumberAnalyzer(n)
        result = analyzer.analyze_numbers()

        self.result_text.delete(1.0, tk.END)
        for number in result:
            self.result_text.insert(tk.END, f"{number}\n")


class NumberAnalyzer:
    def __init__(self, n):
        self.n = n
        self.is_odd_digit = lambda num: num % 10 % 2 == 1 and int(str(num)[0]) % 2 == 1
        self.digit_sum_divisible_by_3 = lambda num: sum(map(int, str(num))) % 3 == 0

    def analyze_numbers(self):
        result = []
        for i in range(1, self.n + 1):
            if self.is_odd_digit(i) and self.digit_sum_divisible_by_3(i):
                result.append(i)
        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberAnalyzerGUI(root)
    root.mainloop()
