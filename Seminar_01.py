"1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого."

"Это сделал я "  "** 2 - в квадрате"
# number1 = int(input())
# number2 = int(input())
# if number2 == number1 ** 2 or number1 == number2 ** 2:
#    print('Yes')
# else:
#    print('No')

"2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них."

# some_list = []
# for _ in range(5):  # 0, 1, 2, 3, 4 искуственно создали последовательность "_"
#     x = int(input())
#     some_list.append(x)  # внести в список х

# print(max(some_list))

# maxx = some_list[0] # Описание print(max(some_list))
# for el in some_list:
#     if el > maxx:
#         maxx = el
# print(maxx)

# maxx = some_list[0]  # Это у нас решение через индекс
# for ind in range(5):
#     if some_list[ind] > maxx:
#         maxx = some_list[ind]
# print(maxx)

""""Параметры sep, end"""

# print(7, end=', ')
# print(8)
# print(7, 8, 9, sep=', ')
# someList = [1, 2, 3, 4]
# print(*someList, sep=', ')

"Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N"

# x = int(input())
# for i in range(-x, x + 1):
#     print(i, end=', ')

"Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа."

# x = input()
# pos = x.find(',')
# if ',' not in x:
#     print('нет')
# else:
#     print(x[pos + 1])


# a = input()
# if '.' in a:
# ind = a.index('.')
# print(a[ind + 1])
# else:
# print('нет')

"Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30."

# x = int(input())
# if (x % 5 == 0 and x % 10 == 0 or x % 15 == 0) and x % 30 != 0:
#     print('da')
# else:
#     print('net')

"Напишите программу, которая принимает на вход цифру, обозначающую день недели," \
" и проверяет, является ли этот день выходным."

# a = int(input())
# if 1 <= a <= 5:
#     print('net')
# else:
#     print('da')

"Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."

# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             print(f'{x} {y} {z} -> {not(x or y or z) == (not x and not y and not z)} ')

"Напишите программу, которая принимает на вход координаты точки (X и Y),"
" причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,"
" в которой находится эта точка (или на какой оси она находится)."

# x, y = int(input()), int(input())
# if x == 0 and y == 0:
#     print('uncurrent')
# elif x == 0:
#     print('OY')
# elif y == 0:
#     print('OX')
# elif x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

"Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов."

# n = int(input())
# print('Для n =',  n, end=': ')
# for i in range(n):
#     print((-3) ** i, end=',')
# print((-3) ** (n - 1))

"Для натурального n создать  индекс-значение, состоящий из элементов последовательности 3n + 1."

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# N = int(input())
# print('Для N =', N, ':  {', end=' ')
# for i in range(N):
#     print(3 * i + 1, end=', ')
# print(3 * N + 1, '}')

"Напишите программу, в которой пользователь будет задавать две строки,"
" а программа - определять количество вхождений одной строки в другой."

# a = 'Я чуть чуть задержался на второй работе'
# b = 'чуть'
# print(a.count(b))

"Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число."

# string = input('Введите строку')
# simbol = input()
# sin_list = ''
# word_list = string.split(' ')
# for i in word_list:
#     for j in i:
#      if j == simbol:
#          print('yes')
# print('No')

"Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет."

# a = input().split()
# find_str = input()
# count = 0
# for i in range(len(a)):
#     if a[i] == find_str:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(-1)
