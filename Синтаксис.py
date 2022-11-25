# # типы данных и переменная
# # int, float, boolean, str, list, None

# # value = None
# # a = 123
# # b = 1.23
# # print(a)
# # print(b)
# # value=12345
# # print(value)

# # чтобы узнать тип переменной
# value = None
# # print(type(value))

# # print(type(a))
# # print(type(b))
# a = 123
# b = 1.23
# value = 12345
# # print(type(value))
# s = 'hello world'
# print(s)  # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s)) # формат
# print(f'{a} - {b} - {s}') # интерполяция
# print('{1} - {2} - {0}'.format(a, b, s)) # можно поменять порядок выведения печати
# f=True
# print(f)


# # list = [1, 2, 3]  # списки (массивы)
# list = ['1', '2', '3', ]
# col= ['hello', 1, 2, 3, 4.5, True]
# print(list)
# print(col)

# Ввод и вывод данных
# print, input

# print('Введите a')
# # a = int(input()) # для целых чисел
# a = float(input()) # для вещественных значений
# print('Введите b')
# # b = int(input()) # для целых чисел
# b = float(input()) # для вещественных значений
# print(a, '+', b, '=', a+b)
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')


# Арифметические операции
# +, -, *, /, %, //, **
# **, ⊕, ⊖, *, /, //, %, +, -
# () Скобки меняют приоритет
# round - округление по математическим правилам
# a = 1.3
# b = 3
#c = round(a*b, 3) # 3 - количество знаков после запятой
# print(c)

# Сокращенные операции
# a = 3
# # a=a+5
# a = a*6
# print(a)


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func=1
# T=4
# x=123
# print(func<T<x)

# f=1>2 or 4<6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# # is_odd = f[1] % 2 == 0  # проверка четности числа
# is_odd = not f[1] % 2 # можно записать вот так
# print(is_odd)


# Управляющие конструкции
# if, if-else

# a=int(input('a = '))
# b=int(input('b = '))
# if a>b:
#     print('Наибольшее число', a)
# else:
#     print('Наибольшее число', b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет,', username)


# Управляющие конструкции While

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции While-else

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)
# # Пожалуй
# # хватит )
# #

# Управляющие конструкции for

# for i in 1, 2, 3, 4, 5:
#     print (i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**2)

# r=range(10)
# for i in r:
#     print(i)

# Строки


# text = 'съешь ещё этих мягких французских булок'
# print(len(text))                 # 39
# print('ещё' in text)             # True
# print(text.isdigit())            # False
# print(text.islower())            # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                           # c
# print(text[1])                           # ъ
# print(text[len(text)-1])                 # к
# print(text[-5])                          # б
# print(text[:])                           # print(text)
# print(text[:2])                          # съ
# print(text[len(text)-2:])                # ок
# print(text[2:9])                         # ешь ещё
# print(text[6:-18])                       # ещё этих мягких
# print(text[0:len(text):6])               # сеикакл
# print(text[::6])                         # сеикакл
# text = text[2:9] + text[-5] + text[:2]   # ...

## Списки: введение
## list = list
# numbers = [1, 2, 3, 4, 5]

# Урок 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# Lambda - анонимный метод функции

""" def f(x):
    return x**2
g = f

print(type(f))
print(type(g))  

def calc(x):
    return x+10
#print(calc(10))

def calc2(x):
    return x*10
#print(calc(10))

def math(op, x):
    print(op(x))

math(calc2, 10)
math(calc, 10)  """

""" def sum(x, y):
    return x+y """

""" sum = lambda x, y: x+y """

""" def mylt(x, y):
    return x*y """

""" mylt = lambda x, y: x*y """

""" def calc(op, a, b):
    print(op(a, b))
    #return op(a, b)
    
calc(lambda x, y: x+y, 4, 5) # Вызов без присваивания функции в переменную """

# List Comprehension
#[exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]


""" my_list = []
 """
""" for i in range(1, 101):
    # if (i%2==0):
    my_list.append(i)
print(my_list) """

""" def f(x):
    return x**3

my_list = [(i, f(i)) for i in range(1, 20) if i % 2 == 0]
print(my_list) """

""" def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)
print(res) """

# map() — это встроенная функция Python,
# позволяющая обрабатывать и преобразовывать все элементы в итерируемом объекте без цикла for

""" li = [x for x in range(1, 20)]
li = list(map(lambda x: x+10, li))
print(li) 

data = list(map(int, input('enter: ').split()))

for e in data:
    print(e)

print('--')
for e in data:
    print(e) """

""" def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = list(map(int, data))
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res) """

# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

""" data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))
print(res) """


""" data = '1 2 3 5 8 15 23 38'.split()
res = list(map(int, data))
res = list(filter(lambda x: not x % 2, res))
res = list(map(lambda x: (x, x**2), res))
print(res) """

# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.

""" users = ['1', '2', '3', '4', '5']
ids = [4, 5, 9, 14, 7]

data = list(zip(users, ids))
print(data) """

# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных. (нумерует кортежи с 0)

users = ['1', '2', '3', '4', '5']
ids = [4, 5, 9, 14, 7]

data = list(enumerate(ids))
print(data)
# print(numbers)                  # [1, 2, 3, 4, 5]
# ran = range(1,  6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)                  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                    # [20, 4, 6, 8, 10]
# print(numbers)                  # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# del colors[0]

# Функции

""" def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return """

# arg = 2.3
# print(f(arg))
# print(type(f(arg)))

# Файлы:

""" colors = ['red', 'green', 'blue']
data = open('fale.txt', 'w')
# data.writelines(colors) # разделителей не будет
data.write('\nLINE 2 \n')
data.write('LINE 3 \n')
data.close() """

# или

"""with open('fale.txt', 'a') as data:
    data.write('\nLINE 245 \n')
    data.write('LINE 378 \n') """

# Чтение файла

""" path = 'fale.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close() """

# Функции и модули:

""" def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5))
print(new_string('!'))
print(new_string(5)) """

""" def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w'))
print(concatenatio('a', '1')) """

#Рекурсия:
#Числа фибоначчи

""" def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
my_list = []
for e in range(1, 10):
    my_list.append(fib(e))
print(my_list) """

# Кортежи:
#Это неизменяемые списки

""" a = (3, 6, 7, 4)
print(a[-2])
t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue') 

t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not suppor item assignment

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue """

# Словари:
# Неупорядоченные коллекции произвольных объектов с доступом по ключу
dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# Множества:
# Неупорядоченная совокупность элементов

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

# Неизменяемое множество

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
