# '''Первая задача'''
# def palindrom(num):
#     num = abs(num)
#     list_num = list(str(num))
#     for i in range((int(len(list_num) / 2))):
#         #print(list_num[i], list_num[-i - 1], i)
#         if list_num[i] != list_num[-i - 1]:
#             return False
#     return True
#
#
# while True:
#     number = int(input('Введите число: '))
#     if number == -1:
#         break
#     else:
#         print(palindrom(number))

# '''Вторая задача'''
# def three_lists(list_num):
#     a = {int(i) for i in list_num if int(i) % 2 == 0 and int(i) != 0}
#     b = {int(i) for i in list_num if int(i) % 3 == 0 and int(i) != 0}
#     c = {int(i) for i in list_num if int(i) % 5 == 0 and int(i) != 0}
#     return a, b, c
#
# num = list(input('Введите числа через запятую:').split(', '))
# print(three_lists(num))

# '''Третья задача'''
# def obratnoe(num):
#     if abs(num) / 10 < 1:
#         return num
#     else:
#         result = ""
#         if num < 0:
#             num = abs(num)
#             result += '-'
#         num = list(str(num))
#         for i in range(len(num)):
#             if num[-i-1] == '0':
#                 continue
#             result += num[-i-1]
#     return result
#
# while True:
#     number = input('(stop - завершение программы)\nВведите число: ')
#     if number == 'stop':
#         break
#     print(obratnoe(int(number)))

# '''Четвёртая задача'''
#
# def root_N(num, deg, accur):
#     x0 = num / deg
#     x1 = (1 / deg) * ((deg - 1) * x0 + num / (x0 ** (deg - 1)))
#     while abs(x1 - x0) > accur:
#         x0 = x1
#         x1 = (1 / deg) * ((deg - 1) * x0 + num / (x0 ** (deg - 1)))
#
#     return str(x1)
#
#
# degree = int(input('Введите степень кореня: '))
# number = int(input('Введите число из которого нужно извлечь корень {}-ой степени: '.format(degree)))
# accuracy = int(input('Введите с какой точностью должен быть посчитан корень: '))
#
# accuracy = 1 / (10 ** accuracy)
# print('Результат: ' + root_N(number, degree, accuracy))


# '''Пятая задача'''
# def simple_or_not(num):
#     count = 2
#     while count <= num and num % count != 0:
#         count += 1
#     return count == num
#
# while True:
#     try:
#         number = int(input('Введите число от 0 до 100000: '))
#         if number == -1:
#             break
#         print(simple_or_not(number))
#     except ValueError:
#         print('Введите число!')

