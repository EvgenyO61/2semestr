# В матрице найти сумму элементов второй половины матрицы

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

rows = len(matrix)
cols = len(matrix[0])

start_row = rows // 2

sum_second_half = sum(sum(row[start_row:]) for row in matrix)

print("Сумма элементов во второй половине матрицы:", sum_second_half)
