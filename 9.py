import tkinter as tk


def show_success_window():
    success_window = tk.Toplevel(root)
    success_window.title("Регистрация успешна")
    success_label = tk.Label(success_window, text="Вы успешно зарегистрированы!")
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


root = tk.Tk()
root.title("Окно регистрации")
root.geometry("300x200")
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

submit_button = tk.Button(root, text="Зарегистрироваться", command=show_success_window)
submit_button.pack()

root.mainloop()
