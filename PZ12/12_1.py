# 1.В последовательности на n целых чисел умножить все элементы на первый
# элемент.

def multiply_first_element(sequence):
    if len(sequence) < 1:
        return sequence

    first_element = sequence[0]
    multiplied_sequence = [x * first_element for x in sequence]

    return multiplied_sequence


sequence = [2, 4, 6, 8, 10]
result = multiply_first_element(sequence)
print(result)