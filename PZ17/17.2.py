#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 2 – 9.

import tkinter as tk
from tkinter import messagebox


def check_values():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a == -b or a == -c or b == -c:
            messagebox.showinfo("Результат", "True")
        else:
            messagebox.showinfo("Результат", "False")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите валидные числа")


# Создание основного окна
window = tk.Tk()
window.title("Проверка чисел на противоположность")

# Метки и поля для ввода чисел
tk.Label(window, text="Введите первое число:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Введите второе число:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Введите третье число:").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(window)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# Кнопка для проверки значений
check_button = tk.Button(window, text="Проверить", command=check_values)
check_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()