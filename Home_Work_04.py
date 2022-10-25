# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('Чтобы составит список простых множителей натурального числа N, введите это число! ')
n = int(input("Введите число N: "))
numbers = []
a = 2
m = n
while a * a <= n:
        if n % a == 0:
            numbers.append(a)
            n//=a
        else:
            a += 1
numbers.append(n)
print(f'Cписок простых множителей числа {m} = {numbers}')

#32. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

def nonRepeatingElements(my_list):
    outputList = []
    for i in range(0, len(my_list)):
        if i == 0:
            if not (my_list[i] in my_list[i + 1 :]):
                outputList.append(my_list[i])
        elif i == len(my_list) - 1:
            if not (my_list[i] in my_list[:i]):
                outputList.append(my_list[i])
        else:
            if not ((my_list[i] in my_list[:i]) or (my_list[i] in my_list[i + 1 :])):
                outputList.append(my_list[i])
    return outputList
my_list = [1, 3, 8, 20, 67, 15, 20, 8, 1]
print(f"Список неповторяющихся чисел последовательности {my_list} -> {nonRepeatingElements(my_list)}")

# 33. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
from random import randint

print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
k = int(input("Введите степень k: "))
factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))
result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1
result.pop(-1)
result.append('=0')
record = open('data.txt', 'w')
record.write(''.join(result))
record.close()

# 34. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def sumPoly (polinomial1, polinomial2):
    for i in range(len(polinomial1)):
        for j in polinomial2:
            if polinomial1[i][1] == j[1]:
                polinomial1[i] = ((polinomial1[i][0] + j[0], polinomial1[i][1]))
                polinomial2.remove(j)
    sum = polinomial1 + polinomial2
    for i in sum:
        if i[0] == 0:
            sum.remove(i)
    sum = sorted(sum, key=lambda num: num[1])
    sum.reverse()
    return sum

with open("poly1.txt", "r") as f:
    M1 = []
    i = 0
    for line in f:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        M1 = M1 + [lst]
print("M1 = ", M1)

with open("poly2.txt", "r") as f2:
    M2 = []
    i = 0
    for line in f2:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        M2 = M2 + [lst]
print("M2 = ", M2)

res = open('sumPoly.txt', 'w')
result = sumPoly(M1, M2)
print(f'Сумма многочленов в виде списка кортежей: {result}')
res.write(str(result))

f.close()
f2.close()
res.close()