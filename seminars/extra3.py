# Напишите программу, которая принимает два множества и выводит все элементы первого, которых нет во втором.

a = {1, 5, 1, 8}
b = {1, 5, 7, 9}
# c = set()
# for elem in a:
#     if elem not in b:
#         c.add(elem)
# print(*c)
print(*(a - b))
print(*(a | b))
print(*(a & b))
