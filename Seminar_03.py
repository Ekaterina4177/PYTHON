# 19. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

""" my_list = ["123", "8", "97", "9", "привет", "росток"]
print('Задан список =',my_list)
number = input('Введите число, слово или символ для поиска в списке: ')
flag = False
for i in my_list:
    if i == number:
        flag = True 
        if flag:
            print(f'Число {number} присутствует в списке')
if flag == False:
    print(f'Число {number} не присутствует в списке') """

# 20. Вывести список, содержащий средние арифметические значения 
# чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

""" numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
my_list = []
for i in numbers:
    my_list.append(sum(i)/len(i))
print('Среднее арифметическое каждого кортежа =', my_list) """

#21. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
#Пример:
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1

""" my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
symbol = input('Введите искомый символ: ')
if symbol in my_list:
    a = my_list.index(symbol) 
    for i in range(a + 1, len(my_list)):
        if my_list[i] == symbol:
            print(i)
            break
        else: 
            print('-1')
else: 
            print('-1') """

str1 = "qwe"
str2 = "qwe", "asd", "zxc", "qwe", "ertqwe"

def get_sec_entry(str1, str2):
    start = str2.index(str1)
    return str2.index(str1, start + 1)

print(get_sec_entry(str1, str2))


#Создать базу данных для продукта: id, name, date
#Сделать функционал для пользователя:
#Предложить выбор: удаление, добавление, поиск товара по id, 
# выход из программы

""" program = True

dictionary = {
    1: {'name': 'Молоко', 'date': '12.04'},
    2: {'name': 'Кефир', 'date': '5.07'},
    3: {'name': 'Хлеб', 'date': '3.07'},
    4: {'name': 'Мясо', 'date': '24.08'},
    5: {'name': 'Яйца', 'date': '11.01'}
}

while program:
    print('1. View\n2. Add\n3. Remove\n4. Exit\n')

    choice = input('Выберите параметр\n')

    if choice == '4':
        program = False

    if choice == '1':
        id = int(input('Input id: '))
        print(f'\n{dictionary[id]}\n')

    if choice == '2':
        id = int(input('\nInput id: '))
        new_name = input('\nInput name: ')
        new_date = input('\nInput date: ')
        dictionary[id] = {'name': new_name, 'date': new_date}

    if choice == '3':
        id = int(input('Input id: '))
        del dictionary[id] """