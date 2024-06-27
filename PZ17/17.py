#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk

def submit():

    pass

def cancel():
    # Логика для обработки данных при нажатии кнопки Cancel
    window.quit()

window = tk.Tk()
window.title("Sign Up")
window.resizable(False, False)

# Настройка стилей
style = ttk.Style()
style.configure('TButton', padding=6, relief="flat", background="#f0ad4e")
style.configure('TLabel', background='#2c3e50', foreground='white', font=('Helvetica', 10))
style.configure('TEntry', padding=6, relief="flat")

# Фрейм для размещения всех виджетов
frame = tk.Frame(window, bg='#2c3e50')
frame.pack(padx=10, pady=(10, 0), fill='x')

# Заголовок
title = tk.Label(frame, text="Sign Up", bg='#f0ad4e', font=('Helvetica', 16))
title.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')

# Поля для ввода данных
labels = ['First Name', 'Last Name', 'Screen Name', 'Date of Birth', 'Gender', 'Country', 'E-mail', 'Phone', 'Password', 'Confirm Password']
entries = {}

for i, label_text in enumerate(labels):
    label = ttk.Label(frame, text=label_text)
    label.grid(row=i+1, column=0, padx=5, pady=5, sticky='e')
    if label_text == 'Date of Birth':
        dob_frame = tk.Frame(frame, bg='#2c3e50')
        dob_frame.grid(row=i+1, column=1, pady=5, sticky='w')
        month = ttk.Combobox(dob_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], width=8)
        month.set("May")
        month.pack(side='left')
        day = ttk.Combobox(dob_frame, values=list(range(1, 32)), width=3)
        day.set(5)
        day.pack(side='left')
        year = ttk.Combobox(dob_frame, values=list(range(1900, 2024)), width=5)
        year.set(1985)
        year.pack(side='left')
        entries[label_text] = (month, day, year)
    elif label_text == 'Gender':
        gender_frame = tk.Frame(frame, bg='#2c3e50')
        gender_frame.grid(row=i+1, column=1, pady=5, sticky='w')
        gender = tk.StringVar()
        male_rb = tk.Radiobutton(gender_frame, text="Male", variable=gender, value="Male", bg='#2c3e50', foreground='white', selectcolor='#2c3e50')
        male_rb.pack(side='left')
        female_rb = tk.Radiobutton(gender_frame, text="Female", variable=gender, value="Female", bg='#2c3e50', foreground='white', selectcolor='#2c3e50')
        female_rb.pack(side='left')
        gender.set("Male")
        entries[label_text] = gender
    elif label_text == 'Country':
        country = ttk.Combobox(frame, values=["USA", "Canada", "UK", "Australia", "Other"], width=17)
        country.set("USA")
        country.grid(row=i+1, column=1, pady=5, sticky='w')
        entries[label_text] = country
    else:
        entry = ttk.Entry(frame, show='*' if 'Password' in label_text else '')
        entry.grid(row=i+1, column=1, padx=5, pady=5, sticky='ew')
        entries[label_text] = entry

# Checkbox
terms = tk.Checkbutton(frame, text="I agree to the Terms of Use", bg='#2c3e50', foreground='white', selectcolor='#2c3e50')
terms.grid(row=len(labels)+1, column=0, columnspan=2, pady=5, sticky='w')

# Кнопки
button_frame = tk.Frame(frame, bg='#2c3e50')
button_frame.grid(row=len(labels)+2, column=0, columnspan=2, pady=10)
submit_button = ttk.Button(button_frame, text="Submit", command=submit)
submit_button.pack(side='left', padx=5)
cancel_button = ttk.Button(button_frame, text="Cancel", command=cancel)
cancel_button.pack(side='left', padx=5)

window.mainloop()
