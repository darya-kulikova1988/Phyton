# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

massive = [0, -1, 5, 2, 3]
count = 0
for i in range(len(massive)-1):
    if massive[i+1] > massive[i]:
        count += 1
print(count)
