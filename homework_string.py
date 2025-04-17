from random import randint
# text = input('please enter some text \n')
#
# word_1 = input('please wnter first word which contain text: ')
# word_2 = input('please wnter second word which contain text: ')
# word_3 = input('please wnter third word which contain text: ')
#
# new_list = []
# list = text.split(' ')
# for i in list:
#     if i.lower() == word_1.strip().lower():
#             new_list.append(i.upper())
#     elif i.lower() == word_2.strip().lower():
#             new_list.append(i.upper())
#     elif i.lower() == word_3.strip().lower():
#             new_list.append(i.upper())
#     else:
#         new_list.append(i)
# print(' '.join(new_list))
# -----------------------------------------------

# проверка фразы на полиндромность (отинаково читается с двух сторон)
# frase = input('please enter a polindrom frase: ')
# modified_frase = frase.replace('.','').replace(',','').replace(';','').replace(' ', '').replace('-','').lower()
# print(modified_frase)
# if modified_frase == modified_frase[::-1]:
#     print('frase is polindrom -', frase)
# else:
#     print('ftase is not a polindrom', frase)
# --------------------------------

# расчет min и max значения, count положительных и отрицательных значений
# list = []
# lenth = 20
# negative_count = 0
# positive_count = 0
# zero_count = 0
#
# for i in range(lenth):
#     list.append(randint(-100, 100))
# print(list)
# print('min vallue from the list =', min(list))
# print('max vallue from the list =', max(list))
# for j in list:
#     if j < 0:
#         negative_count +=1
#     elif j > 0:
#         positive_count +=1
#     else:
#         zero_count +=1
# print('positive values count =', positive_count)
# print('negative values count =', negative_count)
# print('zero values count =', zero_count)
# ---------------------------------------
list= []
sum=0
minus=0
multy=0
devision=0
arithmetic = input(' please enter one arithmetic expression with *,/,+,-\n').strip()
if arithmetic.find('*') != -1:
    list = arithmetic.split('*')
    if list[0].isdigit() and list[1].isdigit():
        multy = int(list[0]) * int(list[1])
        print(multy)
elif arithmetic.find('/') != -1:
    list = arithmetic.split('/')
    if list[0].isdigit() and list[1].isdigit() and int(list[1]) !=0:
        devision = int(list[0]) / int(list[1])
        print(devision)
    else:
        print('error devision by zero')
elif arithmetic.find('+') != -1:
    list = arithmetic.split('+')
    if list[0].isdigit() and list[1].isdigit():
        sum = int(list[0]) + int(list[1])
        print(sum)
elif arithmetic.find('-') != -1:
    list = arithmetic.split('-')
    if list[0].isdigit() and list[1].isdigit():
        minus = int(list[0]) - int(list[1])
        print(minus)
else:
    print('please enter correct expression')

# ------------------------

# expression = input("Введіть арифметичний вираз (наприклад, 23+12): ").strip()
# for operator in ['+', '-', '*', '/']:
#     if operator in expression:
#         num1, num2 = expression.split(operator)
#
#         if num1.isdigit() and num2.isdigit():
#             num1, num2 = int(num1), int(num2)
#
#             if operator == '+':
#                 result = num1 + num2
#             elif operator == '-':
#                 result = num1 - num2
#             elif operator == '*':
#                 result = num1 * num2
#             elif operator == '/':
#                 if num2 == 0:
#                     print("Помилка: ділення на нуль!")
#                 else:
#                     result = num1 / num2
#             print(f"Результат: {result}")
#             break
#         else:
#             print("Помилка: невірний формат чисел!")
#             break
# else:
#     print("Помилка: невірний формат виразу!")