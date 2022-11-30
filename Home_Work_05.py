#Задача на конфетки

from random import randint
print('Игра заключается в том, чтобы взять как можно больше конфет со стола. \nПобеждает тот у кого окажется больше всего конфет')
player_1 = input('Введите имя первого игрока: ')
print('Привет,', player_1.lower().capitalize())
player_2 = input('Введите имя второго игрока: ')
print('Привет,', player_2.lower().capitalize())

def rand(name1, name2):
    priority = randint(1, 2)
    if priority == 1:
        print('Жеребьевкой первый ход достается игроку', name1)
    else:
        print('Жеребьевкой первый ход достается игроку', name2)
    return priority

candy_count = randint(28, 100)
print('На столе лежит', candy_count, 'конфет')

def step(count_candy, pr, name1, name2, cnt1=0, cnt2=0):
    while count_candy > 28:
        if pr == 1:
            count1 = int(input(f'Игрок {name1} введите количество конфет, которое возьмете со стола: '))
            cnt1 += count1
            count_candy -= count1
            print(print_step(player_1.capitalize(), count1, cnt1, count_candy))
            pr = 2
        else:
            count2 = int(input(f'Игрок {name2} введите количество конфет, которое возьмете со стола: '))
            cnt2 += count2
            count_candy -= count2
            print(print_step(player_2.capitalize(), count2, cnt2, count_candy))
            pr = 1
    return pr


    
def print_step(name,count, cnt, count_candy):
    print(f'Игрок {name} взял со стола {count}, теперь у него {cnt} конфет. Осталось на столе {count_candy}')

        
play = step(candy_count, rand(player_1.capitalize(), player_2.capitalize()), player_1.capitalize(), player_2.capitalize())
if play == 1:
    print('Победил игрок -', player_1.capitalize())
else:
    print('Победил игрок -', player_2.capitalize())
    
    
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах

with open ('HM5.txt', 'r', encoding='utf8') as read:
    one = read.readline()
two = one.replace('', '1')
with open ('HM5-1.txt', 'w', encoding='utf8') as write:
    first = write.write(two)
free = two.replace('1', '')
with open ('HM5.txt', 'w', encoding='utf8') as write:
    first = write.write(free)
