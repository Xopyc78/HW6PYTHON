# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9
a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1+i*d)
