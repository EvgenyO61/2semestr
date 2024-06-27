#перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно

import os

# Получаем домашний каталог текущего пользователя
home_directory = os.path.expanduser('~')

# Путь к целевому каталогу
target_directory = os.path.join('/home/student/Документы/uc27klipan/pz', 'pz 11')

# Проверяем существование каталога
if os.path.exists(target_directory) and os.path.isdir(target_directory):
    # Получаем список всех файлов в целевом каталоге
    files = [f for f in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, f))]

    # Выводим список файлов
    for file in files:
        print(file)
else:
    print(f"The directory '{target_directory}' does not exist.")
