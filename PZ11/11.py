# Средствами языка Python сформировать текстовый файл(.txt), содержащий последовательность из целых положительных и
# отрицательных чисел.Сформировать новый текстовый файл(.txt) следующего вида, предварительно выполнив требуемую обработку
# элементов:
import random

sequence = [random.randint(-100, 100) for _ in range(10)]

with open("sequence.txt", "w") as file:
    file.write("Исходные данные:\n")
    file.write(" ".join(map(str, sequence)))

min_value = min(sequence)
last_min_index = len(sequence) - 1 - sequence[::-1].index(min_value)

multiplied_sequence = [element * sequence[0] for element in sequence]

with open("result.txt", "w") as file:
    file.write("Исходные данные:\n")
    file.write(" ".join(map(str, sequence)))
    file.write('\n')
    file.write('\n')
    file.write("Количество элементов: {}\n".format(len(sequence)))
    file.write("Индекс последнего минимального элемента: {}\n".format(last_min_index))
    file.write("Умножаем все элементы на первый элемент:\n")
    file.write(" ".join(map(str, multiplied_sequence)))
