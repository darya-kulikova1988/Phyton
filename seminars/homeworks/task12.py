# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4   -> 2 2
# 5 6   -> 2 3
# 6 9   -> 3 3
# 7 12  -> 3 4
# 11 30 -> 5 6

# s = int(input("Введите сумму чисел S: "))
# p = int(input("Введите произведение чисел P: "))
# d = s*s-4*(p)
# x1 = int((s+pow(d, 0.5))/2)
# x2 = int((s-pow(d, 0.5))/2)
# print(f'{s} {p} --> {x1} {x2}')

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)
