# Задача 8: Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один
# разлом по прямой между дольками(то есть разломить шоколадку на два прямоугольника).

# *Пример: *
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите размер шоколадки по высоте: "))
m = int(input("Введите размер шоколадки по ширине: "))
k = int(input("Введите размер отломленных долек: "))
if k == m*n:
    print(f'Шоколадка целиком')
elif k > m*n:
    print(f'Количество долек превышает размер шоколадки')
else:
    if k % n == 0 or k % m == 0:
        print(f'{n} {m} {k} -> yes')
    else:
        print(f'{n} {m} {k} -> no')
