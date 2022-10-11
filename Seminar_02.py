# Метод	                Что делает:
# list.append(x)        Добавляет элемент в конец списка
# list.extend(L)        Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x) 	Вставляет на i-ый элемент значение x
# list.remove(x)        Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])         Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]])  Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)         Возвращает количество элементов со значением x
# list.sort([key=функция])  Сортирует список на основе функции
# list.reverse()        Разворачивает список
# list.copy()           Поверхностная копия списка
# list.clear()          Очищает список 


# 1. Выяснить, является ли число кратным заданному, если нет, вывести остаток.
"""
print('Выяснить, является ли число кратным заданному, если нет, вывести остаток.')
print()
number_default = 25
number_user = int(input(f'Введите число для проверки кратности к числу {number_default}: '))
print()
if number_user == 0:
    print(f'Ошибка. Введенное пользователем число равно нулю')
elif number_default == number_user:
    print(f'Числа равны между собой')
elif number_default % number_user == 0:
    print(f'Введенное пользователем число "{number_user}" кратно заданному числу "{number_default}"')
elif number_user % number_default == 0:
    
    print(f'Заданное число "{number_default}" кратно введенному пользователем числу "{number_user}"')
else:
    remains_one = number_default % number_user
    remains_two = number_user % number_default 
    if number_default > number_user:
        print(f'Введенное число "{number_user}" не кратно заданному числу "{number_default}" и его остаток равен "{remains_one}"')
    elif number_default == number_user:
        print(f'Числа равны между собой')
    else:
        print(f'Заданное число "{number_default}" не кратно введенному числу "{number_user}" и его остаток равен "{remains_two}"')
print() """
# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

""" N = int(input('Введите число: '))
for i in range(N):
    result = (-3)**i
    print(result, end=" ") """


# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

""" my_dict = {}
my_dict[1] = 4
n = int(input('Введите число: '))
for i in range(1, n + 1):
    my_dict[i] = 3*i + 1
print(my_dict, end=' ')  """

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

""" string_one = "Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой."
string_two = "а"
result = string_one.count(string_two)
print(f'Количество строки "{string_two}"',result)  """