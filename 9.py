import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def show_success_window_reg():
    username = entry_username.get()
    password = entry_password.get()

    if not username.strip() or not password.strip():
        messagebox.showerror("Ошибка", "Пожалуйста, введите имя пользователя и пароль.")
    else:
        success_window = tk.Toplevel(root)
        success_window.title("Регистрация успешна")
        success_label = tk.Label(success_window, text="Вы успешно зарегистрированы!")
        success_label.pack()

        ok_button = tk.Button(success_window, text="Окей", command=close_all_windows)
        x = (success_window.winfo_screenwidth() - success_window.winfo_reqwidth()) // 2 + 75
        y = (success_window.winfo_screenheight() - success_window.winfo_reqheight()) // 2 + 50
        success_window.geometry("+%d+%d" % (x, y))
        ok_button.pack()


def show_success_window():
    username = entry_username.get()
    password = entry_password.get()

    if not username.strip() or not password.strip():
        messagebox.showerror("Ошибка", "Пожалуйста, введите имя пользователя и пароль.")
    else:
        success_window = tk.Toplevel(root)
        success_window.title("Вход выполнен успешно")
        success_label = tk.Label(success_window, text="Вы успешно вошли в аккаунт!")
        success_label.pack()

        ok_button = tk.Button(success_window, text="Окей", command=close_all_windows)
        x = (success_window.winfo_screenwidth() - success_window.winfo_reqwidth()) // 2 + 75
        y = (success_window.winfo_screenheight() - success_window.winfo_reqheight()) // 2 + 50
        success_window.geometry("+%d+%d" % (x, y))
        ok_button.pack()


def close_all_windows():
    root.destroy()
    new_empty_window = tk.Tk()
    new_empty_window.title("Пустое окно")
    new_empty_window.geometry("400x200")
    x = (new_empty_window.winfo_screenwidth() - new_empty_window.winfo_reqwidth()) // 2
    y = (new_empty_window.winfo_screenheight() - new_empty_window.winfo_reqheight()) // 2
    new_empty_window.geometry("+%d+%d" % (x, y))


def validate_password_strength():
    password = entry_password.get()
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(char.isalpha() for char in password):
        strength += 1

    if any(not char.isalnum() for char in password):
        strength += 1

    progress_var.set(strength * 25)


root = tk.Tk()
root.title("Окно регистрации")
root.geometry("300x280")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
root.geometry("+%d+%d" % (x, y))

label_username = tk.Label(root, text="Имя пользователя:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Пароль:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

label_strength = tk.Label(root, text="Сложность пароля:")
label_strength.pack()

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, orient='horizontal', length=250, mode='determinate', variable=progress_var,)
progress_bar.pack()

entry_password.bind('<KeyRelease>', lambda event: validate_password_strength())

submit_button = tk.Button(root, text="Войти", command=show_success_window)
submit_button.pack()

submit_button = tk.Button(root, text="Зарегистрироваться", command=show_success_window_reg)
submit_button.pack()

root.mainloop()
