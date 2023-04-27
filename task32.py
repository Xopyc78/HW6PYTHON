# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Input:
# 1, 3, 7, 10, 5, 8 - рассматриваемый список
# 4 - начало диапазона
# 8 - конец
# Output:
# 2(7), 4(5), 5(8)
from random import randint


array=[]
for i in range (randint(5,15)):
    array.append(randint(1,10))
print(array)


start=3
end=7
array2=[]
j=0
while j<len(array):
    if array[j]>=start and array[j]<=end:
        array2.append(j)
    j+=1
print(array2)
