# 1. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ..., 2 кг
# конфет.
while True:
    try:
           price = float(input("Введите цену 1 кг конфет: "))
           break
    except ValueError:
           print('')
           print('нужно ввести число')

for i in range(12, 21, 2):
    weight = i / 10
    cost = price * weight
    if weight >= 1.2 and weight <= 2:
        print("стоимость", weight, "кг конфет:", cost, "рублей")
