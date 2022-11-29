# Задача №1 Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях

print("Введите целые числа через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
sum = 0

for i in range(len(list_numbers)):
    if i % 2 != 0:
        sum = sum + list_numbers[i]

print(f"Сумма чисел, стоящих на нечётных позицииях = {sum}")

# Задача №2 Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число: '))
fac = lambda a, b: a * b
f = 1
print('Набор произведений чисел:')
for i in range(N):
    i += 1
    f = fac(f, i)
    print(f, end=' ')

# Задача №3 Подсчитать суммe чисел в вещественном числе.

from random import uniform

number = round(uniform(1, 100), 2)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(f"Дано вещественное число {number}")
print(f'Сумма цифра в вещественном числе {number} =', sum_digit(number))

# Задача №4 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def multiplied_list(list_numbers):
    l = len(list_numbers)//2 + 1 if len(list_numbers) % 2 != 0 else len(list_numbers)//2
    new_list_numbers = [list_numbers[i]*list_numbers[len(list_numbers)-i-1] for i in range(l)]
    print(new_list_numbers)

print("Введите числа через пробел:", end=' ')
list_numbers = list(map(int, input().split()))
multiplied_list('Полученные пары чисел =', list_numbers)

# Задача №5 Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму.

number = int(input('Введите число: '))

def get_squerence(n):
    return [round((1 + 1 / x )**x, 2) for x in range (1, n + 1)]

nums = get_squerence(number)
print(f'Полученная последовательность из числа "{number}" =', nums)
print('Сумма чисел =', round(sum(nums), 2))
