# filter() фильтрует списки, строки и тд
# Профильтровать список так, чтобы в новом списке появились только строки с буквой (i)

product = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
print('Дан список =', product)

def search_I(elem):
    return elem[0] == 'i'
new_product = list(filter(search_I, product))

print('Отформатированный список =',new_product)
print(*new_product)  # распаковка списка без цикла с символом *

# lambda() - помогает исключить написание функции def.
# Как читается лямбда: lambda(функция def) принимает агрумент (прим. x)
# и возвращает его при условии, что x>0 из указанного списка (прим. numbers строка 20).

numbers = [1, 54, -45, -3, 5, -8, 6]

posit_num = list(filter(lambda x: x > 0, numbers))
negat_num = list(filter(lambda x: x < 0 , numbers))
even_num = list(filter(lambda x: x % 2 == 0, numbers))
uneven_num = list(filter(lambda x: x % 2 != 0, numbers))

print(posit_num,  negat_num, 
      even_num, uneven_num)


# list complectention
# отсортировать слова все, которые больше 4 символов

product = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']

def find_len(el):
    return len(el) > 4 # через функцию def

new_product = [i for i in product if len(i) > 4] # через list complectention создание списка
new_product2 = list(filter(lambda x: len(x) > 4, product)) # через Lambda создание списка
new_product3 = list(filter(lambda x: 'e' in x, product)) # поиск символа 'е' через Lambda создание списка
print(new_product, new_product2, new_product3)

my_dict = {i: x for i, x in enumerate(product) if len(x) > 4} # создание словаря через list complectention
print(my_dict)

# вывести все товары с i через lambda
# lower проверяет нижний и верхний регистр буквы, startswich - поиск символа

product = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
print(*filter(lambda x: 'i' in x, product))
print(*filter(lambda x: x.lower().startswith('i'), product)) 

# map(func, el) принимает функцию и итерируемый объект

# пример умножения каждого элемента на 5:

numbers = [1, 2, 4, 5]
def mult(el):
    return el*5
print(list(map(mult, numbers))) #в списке 
print(*(map(mult, numbers))) # распакованный

# сложение через map() трех списков
# если количество элементов в списке разное, то подсчет идет
# по меньшему кол-ву символов в одном из списков

numbers = [1, 2, 4, 5]
numbers2 = [1, 6, 8, 5]
numbers3 = [9, 2, 6, 5]

def sum(el1, el2, el3):
    return el1 + el2 + el3

print(list(map(sum, numbers, numbers2, numbers3)))

# пример решения задачи на обращения списка в кортеж через map()
# tuple() - кортеж
# float - перевод в комплексное число целое число или строку

prices = ['15.6','5.8','9.1','12.6']
price =tuple(map(float, prices))
print(price)

# map() + Lambda()

numbers = [1, 2, 3, 4, 5, 6]

print(list(map(lambda x: x + 1, numbers))) # прибавляем к каждому элементу списка 1
print(list(map(lambda x: x * 2, numbers))) # умножаем каждый элемент списка на 2
print(list(map(lambda x: x ** 2, numbers))) # возводим во 2 степень каждый элемент списка

# Применить скидку к товарам и округлить до 2 знаков

price = ['45.6', '15.7', '67.8', '123.6']
discont = 7
price = list(map(float, price))
print(list(map(lambda x: round(x * (100-discont)/100, 2), price)))

# фильтрация прайса на ошибки, выдает только элементы без ошибок

price = ['45.6,7', '15.7 rub', '67.8', '123.6 a']

new_price = list(map(float, filter(lambda x: x.replace('.', '', 1).isdigit(), price)))
print(new_price)

# zip() при объединении всгда получает в конце кортеж вида (x, x)

numbers = [1,2,3,4,5]
word = ['a', 'b', 'c', 'd', 'e']
result = zip(numbers, word)
print(*result)

#обрернуть в словарь

numbers = [1,2,3,4,5]
word = ['a', 'b', 'c', 'd', 'e']
result = dict(zip(numbers, word))
print(result)

# вывести информацию по каждому пользователю
#zip_longest не позволяет потеряться информации и там где ее нет в списке пишет None

from itertools import zip_longest
user_names = ['Иван', 'Петр']
user_logins = ['ivan', 'petr', 'olga', 'sergey']
user_roles = ['user', 'staff', 'admin', 'user']
print(list(zip_longest(user_names, user_logins, user_roles)))

# enumerate() возвращает кортеж из индекса элемента и самого элемента переданной ей последовательности (итерируемого объекта).

colors = ['red', 'green', 'blue']
for pair in enumerate(colors):
    print(pair)


#Если счет нужно начать с отличного от нуля числа, то нужно передать значение аргумента start.

colors = ['red', 'green', 'blue']
ind = 5
for k, v in enumerate(colors, ind+1):
    print({k: v})

colors = ['red', 'green', 'blue']

pairs = enumerate(colors)

print(pairs)
print(list(pairs))


colors = ['red', 'green', 'blue']
for index, item in enumerate(colors):
     print(index, item)

# Такой код является альтернативой коду:

colors = ['red', 'green', 'blue']
for i in range(len(colors)):
    print(i, colors[i])
