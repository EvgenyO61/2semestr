# Открываем файл для чтения
with open('price.txt', 'r',encoding="utf-8") as file:
    # Читаем содержимое файла
    content = file.read()

    # Используем регулярные выражения для извлечения всех цен
    import re
    prices = re.findall(r'\d+\.\d{2}', content)

    # Печатаем найденные цены
    print(prices)

    # Подсчитываем количество цен
    count = len(prices)
    print(f'Количество цен: {count}')
