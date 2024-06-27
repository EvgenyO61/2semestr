#Дан целочисленный список размера N. Найти максимальное количество его
#одинаковых элементов.

def max_occurrences(lst):
    if not lst:
        return 0

    occurrences = {}
    max_count = 0

    for num in lst:
        occurrences[num] = occurrences.get(num, 0) + 1
        max_count = max(max_count, occurrences[num])

    return max_count

# Пример использования
N = int(input("Введите размер списка N: "))
my_list = [int(input(f"Введите элемент {i+1}: ")) for i in range(N)]

result = max_occurrences(my_list)
print(f"Максимальное количество одинаковых элементов в списке: {result}")
