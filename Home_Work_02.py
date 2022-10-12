""" # Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print(f"Сумма чисел в числе '{number}' равна:", sum)

#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from unittest import result
result = 1
number = int(input('Введите число: '))
print('Полученный набор чисел:')
for i in range(1, number + 1):
    result *= i
    print(result, end=' ')

#Задайте список из n чисел последовательности (1+1/n)^n 
#и выведите на экран их сумму.
#Пример:
#Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

my_dict = {}
my_dict[1] = 2
number = int(input('Введите число: '))
for i in range(1, number + 1):
    my_dict[i] = round((1+1/i)**i, 2)
print(f'Последовательность из числа "{number}" = ', my_dict)

#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на введенных пользователем позициях.

number = int(input('Введите число: '))
my_list = []
for i in range(-number, number + 1):
    my_list.append(i)
print('Полученный список:', my_list)
number_a = int(input('Введите индекс числа из списка для произведения: '))
number_b = int(input('Введите индекс числа из списка для произведения: '))
result = my_list[number_a] * my_list[number_b]
print(f'Произведение числа "{my_list[number_a]}" на число "{my_list[number_b]}" =' ,result)

# Реализуйте алгоритм перемешивания списка.
 """
import random
my_list = ['red', 'green', 'blue', 'gray', 'red', 'green', 'blue', 'gray']
print ("Дан список = ", my_list)
for i in range(len(my_list)-1, 0, -1):
    j = random.randint(0, i + 2) 
    my_list[i], my_list[j] = my_list[j], my_list[i] 
print ("Список после перемешивания =",  my_list)