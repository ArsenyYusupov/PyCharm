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
