# Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении
# данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из
# них словарь: ключи — ФИО, значения — данные о хобби.

""" Сохранить словарь в файл users_hobby.txt. 
Фрагмент файла с данными о пользователях (users.txt):
Иванов Иван Иванович
Петров Петр Петрович
Фрагмент файла с данными о хобби (hobby.txt):
скалолазание, охота
горные лыжи """

with open ('users.txt', encoding='utf8') as u:
    with open ('hobby.txt', encoding='utf8') as h:
        users = u.readlines()
        hobby = h.readlines()

for i in range(len(users)):
    users[i] = users[i].replace('\n','')

users_hobby = dict(zip(users, hobby))

with open ('users_hobby.txt', 'w', encoding='utf8') as data:
    for key, val in users_hobby.items():
        data.write('{}: {}'.format(key, val))
        

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input('Введите число: '))

def multic(N):
    my_list = []
    dell = 2
    while (N >= dell):
        if N % dell == 0:
            my_list.append(dell)
            N /= dell
        else:
            dell += 1
    print(my_list)
multic(number)


# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import random

my_list = []
for i in range(10):
    my_list.append(int(random()*10))
print(my_list)

my_list_new = []

for i in my_list:
    count = 0
    for j in my_list:
        if i == j:
            count += 1
    if count == 1:
        my_list_new.append(i)
print(my_list_new)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from random import randint

k = int(input('Введите натуральную степень числа k: '))

my_list = []

for i in range(randint(5, 10)):
    my_list.append(randint(1, 10))
print(my_list)

result = ''

for i in range(k-1):
    if k > 1:
        result = result + str(my_list[i]) + 'x' +'^' + str(k) + '+'
        result = result + str(my_list[i+1]) + 'x' + '+'
        result = result + str(my_list[k+1]) + '=' + '0'
        break
    else:
        print('Степень k должна быть больше единицы')

print(result)

with open ('Zadacha4.txt', 'w', encoding='utf8') as data:
    data.write(result)

# *Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0
from itertools import zip_longest
o = open('Zadacha5.txt', 'r', encoding='utf8')
on = o.read()
t = open('Zadacha5-1.txt', 'r', encoding='utf8')
tw = t.read()
print(on)
print(tw)

on = on.replace('+', ' ')
on = on.replace('x*2', '')
on = on.replace('x', '')
on = on.replace('=0', '')
print(on)

tw = tw.replace('+', ' ')
tw = tw.replace('x*2', '')
tw = tw.replace('x', '')
tw = tw.replace('=0', '')
print(tw)

list_on = on.split()
list_tw = tw.split()

sum = [int(list_on[i])+int(list_tw[i]) for i in range(len(list_on))]
print(sum) 

result = ''
for i in range(len(sum)):
    result = result + str(sum[i]) + 'x*2' + '+'
    break
result = result + str(sum[i+1]) + 'x' + '+'
result = result + str(sum[i+2]) + '=0'
print(result)

with open ('Zadacha5-2.txt', 'w', encoding='utf8') as data:
        data.write(result)
