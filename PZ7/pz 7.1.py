#Дано целое положительное число. Вывести символы, изображающие цифры этого
#числа (в порядке слева направо).

def print_digits(number):
    # Преобразование числа в строку
    number_str = str(number)

    # Вывод символов цифр
    print("Символы, изображающие цифры числа:")
    for digit in number_str:
        print(digit)

# Пример использования
positive_integer = int(input("Введите целое положительное число: "))
print_digits(positive_integer)
