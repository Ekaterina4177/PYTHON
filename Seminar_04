# Задайте строку из набора чисел. Запишите ее в файл. 
# Напишите программу, которая считает строку из файла и покажет 
# большее и меньшее число. В качестве символа-разделителя используйте пробел.

numbers = '1 2 6 7 5 3 8 3'

with open ('File_1.txt', 'w') as data:
    data.write(numbers)
with open ('File_1.txt', 'r', encoding='utf8') as data:
    numbers2 = data.read()
print(numbers2.split(' '))

my_list = []
for i in numbers2.split(' '):
    my_list.append(int(i))
print(my_list)
print(max(my_list), min(my_list))

 
# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python
# При этом функцию для нахождения дискриминанта импортируйте из файла utils.py

from math import sqrt

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
def ds(a, b, c):
    ds = b**2 - 4*a*c
    return ds
x1 = round((-b + sqrt(ds(a, b, c))) / 2*a)
x2 = round((-b - sqrt(ds(a, b, c))) / 2*a)
print('x1 =', x1,'x2 =', x2)

#Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите число A: '))
b = int(input('Введите число B: ')) 
def NOK(x, y):
    if a != 0 and b != 0:
        if a > b:
            max = x
        else:
            max = y
        while True:
            if (max % x == 0) and (max % y == 0):
                nok = max
                break
            max += 1
        return nok
    else:
        print('Число не должно быть равно 0')
        
print(NOK(a, b))
