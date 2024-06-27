#перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test

import os
import shutil
import random

# Определение путей
project_root = os.path.abspath(os.path.dirname(__file__))
test_folder = os.path.join(project_root, 'test')
test1_folder = os.path.join(test_folder, 'test1')

# Создание папок test и test/test1
os.makedirs(test1_folder, exist_ok=True)

home_directory = os.path.expanduser('~')

# Определение путей к каталогам ПЗ6 и ПЗ7
pz6_directory = os.path.join('/home/student/Документы/uc27klipan/pz', 'pz 6')
pz7_directory = os.path.join('/home/student/Документы/uc27klipan/pz', 'pz 7')

# Проверка существования каталогов ПЗ6 и ПЗ7
if not os.path.exists(pz6_directory):
    print(f"The directory '{pz6_directory}' does not exist.")
    exit(1)
if not os.path.exists(pz7_directory):
    print(f"The directory '{pz7_directory}' does not exist.")
    exit(1)

# Получение списка всех файлов в каталогах ПЗ6 и ПЗ7
pz6_files = []
for root, dirs, files in os.walk(pz6_directory):
    for f in files:
        pz6_files.append(os.path.join(root, f))

pz7_files = [os.path.join(pz7_directory, f) for f in os.listdir(pz7_directory) if os.path.isfile(os.path.join(pz7_directory, f))]

# Проверка наличия достаточного количества файлов для перемещения
if len(pz6_files) < 2:
    print(f"Not enough files in '{pz6_directory}' to move.")
    exit(1)
if len(pz7_files) < 1:
    print(f"No files found in '{pz7_directory}' to move.")
    exit(1)

# Выбор двух случайных файлов из ПЗ6
random_pz6_files = random.sample(pz6_files, 2)

# Выбор одного случайного файла из ПЗ7
random_pz7_file = random.choice(pz7_files)

# Перемещение выбранных файлов из ПЗ6 в папку test
for file_path in random_pz6_files:
    shutil.move(file_path, test_folder)

# Перемещение и переименование выбранного файла из ПЗ7 в папку test/test1
shutil.move(random_pz7_file, os.path.join(test1_folder))

# Получение списка файлов в папке test
test_files = [f for f in os.listdir(test_folder) if os.path.isfile(os.path.join(test_folder, f))]

# Вывод информации о размере файлов в папке test
print("File sizes in the 'test' folder:")
for file_name in test_files:
    file_path = os.path.join(test_folder, file_name)
    file_size = os.path.getsize(file_path)
    print(f"{file_name}: {file_size} bytes")
