#перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).

import os

# Путь к корневой папке, где находятся pz1 до pz17
home_directory = os.path.expanduser('~')

# Путь к папке PZ11
pz11_directory = os.path.join('/home/student/Документы/uc27klipan/pz', 'pz 11')

# Проверка существования папки PZ11
if not os.path.exists(pz11_directory):
    print(f"The directory '{pz11_directory}' does not exist.")
    exit(1)

# Получение списка файлов в папке PZ11
files_in_pz11 = os.listdir(pz11_directory)

py_files = [f for f in os.listdir(pz11_directory) if f.endswith('.py')]

# Инициализация переменной для хранения имени файла с самым коротким именем
shortest_filename = None
shortest_length = None

# Поиск файла с самым коротким именем
for filename in py_files:
    file_path = os.path.join(pz11_directory, filename)
    file_length = len(filename)  # Длина имени файла
    if shortest_length is None or file_length < shortest_length:
        shortest_filename = filename
        shortest_length = file_length

# Вывод имени файла с самым коротким именем, используя os.path.basename()
if shortest_filename:
    shortest_basename = os.path.basename(shortest_filename)
    print("Shortest filename in PZ11:", shortest_basename)
else:
    print("No .py files found in PZ11 directory.")