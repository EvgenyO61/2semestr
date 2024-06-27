#Дан список размера N, все элементы которого, кроме одного, упорядочены по
#убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
#упорядоченность, на новую позицию.

testing_list = []
list_range = 4

for i in range(list_range):
    testing_list.append(int(input(f"list index {i+1}: ")))

previous = None

for i in testing_list:
    if previous:
        if previous <= i:
            testing_list.remove(previous)
            testing_list = [previous,*testing_list]
    previous = i

print(testing_list)
