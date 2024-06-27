# Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

with open("text18-15 (1).txt", "r", encoding="UTF-16") as file:
    content = file.read()

lowercase_count = sum(1 for char in content if char.islower())

print("Содержимое файла:")
print(content)
print("Количество букв в нижнем регистре:", lowercase_count)

poem = content.upper()

with open("poem.txt", "w") as file:
    file.write(poem)

print("\nСтроки в стихотворном виде были записаны в файл poem.txt.")
