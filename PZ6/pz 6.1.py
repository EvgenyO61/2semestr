#Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
#арифметическое элементов список с номерами от K до L включительно.

def average_between_k_and_l(lst, k, l):
    # Проверка на корректность входных данных
    if not 1 < k < l < len(lst):
        return "Некорректные значения K и L"

    # Выбор подсписка с элементами от K до L
    sublist = lst[k-1:l]

    # Вычисление среднего арифметического
    average = sum(sublist) / len(sublist)

    return average

# Пример использования
N = int(input("Введите размер списка N: "))
my_list = [int(input(f"Введите элемент {i+1}: ")) for i in range(N)]
K = int(input("Введите значение K (1 < K < L < N): "))
L = int(input("Введите значение L (1 < K < L < N): "))

result = average_between_k_and_l(my_list, K, L)

if isinstance(result, str):
    print(result)
else:
    print(f"Среднее арифметическое элементов с номерами от {K} до {L}: {result}")
