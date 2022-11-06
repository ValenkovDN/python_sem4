#Задача № 30. Вычислить число c заданной точностью d
# import math
# a = int(input('Задайте точность числа: '))
# print(f'{round(math.pi, a)}') #для числа пи
#n = float(input('Задайте  число: ')) #для любого дробного числа
# print(f'{float(round(n,a))}')

#Задача № 31. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# n = int(input("Введите число: "))
# i = 2 # первое простое число
# list = []
# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа  приведены в списке: {list}")

#Задача № 32. Задайте последовательность чисел. Напишите программу,
#которая выведет список неповторяющихся элементов исходной последовательности.
# a = list(map(int, input('Введите числа через пробел:' ).split()))
# b = []
# for i in a: 
#     if a.count(i) == 1:
#         b.append(i)
# print(b)

#Задача № 33. Задана натуральная степень k. Сформировать случайным образом список 
#коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# import random
# k = int(input('Введите натуральную степень k: '))
# result = [0 for i in range(k)]
# koef = random.sample(range(0,100), k + 1)
# print(f'Рандомные коэффициенты: {koef}')
# for i in range(len(result)):
#     result[i] = f'{koef[i]}x^{k}'
#     k -= 1
# result.append(str(koef[-1]))
# print(f'До обработки: {result}')
# for j in result:
#     if j == 0:
#         result.remove(j)
#         try:
#             ind_x = j.find('x')
#             d = int(j[:ind_x])
#         except AttributeError:
#             continue
#         if d == 0 or j == '0':
#             result.remove(j)
#         if '^1' in j:
#             result.remove(j)
#             result.insert(-1, j[:j.find('^1')])
# print(f'После обработки: {result}')
# polynom = ''
# for i in range(len(result)-1):
#     polynom += f'{result[i]} + '
# polynom += f'{result[-1]} = 0'
# print(polynom)
# with open('polynom.txt', 'w') as f:
#     f.write(polynom)
