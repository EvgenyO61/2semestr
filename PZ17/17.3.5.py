#удалить файл test.txt

import os

# Определение пути к файлу test.txt
file_path = os.path.join('test', 'test1', 'test.txt')

# Проверка существования файла
if os.path.exists(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except OSError as e:
        print(f"Error deleting file '{file_path}': {e}")
else:
    print(f"File '{file_path}' does not exist.")
