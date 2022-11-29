# def multiply(x, y):
#     print(x * y)
#
#
# multiply(5, 4)


# def multiply(*nums):
#     z = 1
#     for num in nums:
#         z *= num
#     print(z)
#
#
# multiply(4, 5)
# multiply(10, 9)
# multiply(2, 3, 4)
# multiply(3, 5, 10, 6, 10)


# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print("Р—РЅР°С‡РµРЅРёРµ РґР»СЏ {} СЏРІР»СЏРµС‚СЃСЏ {}".format(key, value))
#
#
# print_values(
#     name_1="Alex",
#     name_2="Gray",
#     name_3="Harper",
#     name_4="Phoenix",
#     name_5="Remy",
#     name_6="Val"
# )


# def func(required_arg, *args, **kwargs):
#     print('r_a: ', required_arg)
#
#     if args:
#         print('args: ', args)
#
#     if kwargs:
#         print('kwargs: ', kwargs)
#
# # func()
#
# func("required argument")
#
# func("required argument", 1, 2, '3')
#
# func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")


#from itertools import zip_longest
#
# out_dict = {}
# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     with open('users.txt', encoding='utf-8') as users:
#         with open('hobby.txt', encoding='utf-8') as hobby:
#             for line_user, line_user_hobby in zip_longest(users, hobby):
#                 f.writelines(f'{line_user.strip()}: {line_user_hobby}\n')


# import json
#
# out_dict = {}
# with open('users.txt', encoding='utf-8') as users:
#     with open('hobby.txt', encoding='utf-8') as hobby:
#         for line_user, line_user_hobby in zip_longest(users, hobby):
#             out_dict[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby
#
#
#
# with open('task3.json', 'w', encoding='utf-8') as f:
#     json.dump(out_dict, f, ensure_ascii=False)
# print(out_dict)

"Задачи:"

# Есть список чисел. Вывести – является ли последовательность строго убывающей,
# или строго возрастающей, или ни то, ни другое

sequence = [1, 2, 3, 4, 5, 6, 7]
count = 0


def check_sequence():
    global count
    for i in range(0, len(sequence) - 1):
        if sequence[i+1] - sequence[i] == 1:
            count = 1
        elif sequence[i] - sequence[i+1] == 1:
            count = 2
        else:
            count = 0


check_sequence()

if count == 1:
    print('Строго возрастающая')
elif count == 2:
    print('Строго убывающая')
else:
    print('Ни то, ни другое')


# Дана последовательность чисел. Получить отсортированный по возрастанию список
# уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

sequence = [1, 2, 3, 5, 1, 5, 3, 10]
new_sequence = [i for i in sequence if sequence.count(i) == 1]
print(sorted(new_sequence))


# Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов).
# Двумерный массив заполнен числами от 1 до 9.
# Функция должна вернуть False, если в массиве все числа от 1 до 9 встречаются ровно один раз.
# В противном случае True.
# [[1, 3, 2], [9, 7, 8], [4, 5, 6]] ➞ False
# [[1, 1, 3], [6, 5, 4], [8, 7, 9]] ➞ True # 1 дублируется

mass = [[1, 3, 2], [9, 7, 8], [4, 5, 6]]

new_list = [i for j in mass for i in j] #распаковка двумерного массива через лист комплектейшн
print(sorted(new_list) != [1, 2, 3, 4, 5, 6, 7, 8, 9]) #решение 1

def sort_mass(mtrx):
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = []
    for i in mtrx:
        for j in i:
            arr.append(j)
    sorted_arr = sorted(arr)
    return sorted_arr != array


print(sort_mass(mass)) # решение 2 
