#2. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
деления, найти количество и сумму его цифр.

while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except ValueError:
        print('')
        print('Error: Нужно ввести целое число')
sum_of_digits = 0
count_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    count_of_digits += 1
    num = num // 10

print(f"Количество цифр:",count_of_digits,"сумма цифр:",sum_of_digits)
