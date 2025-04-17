# print('Lesson 29-30 internal function, global & local variables\n')
# from constants import NAMES
#
# size = 4
#
# def geometric_shape(name: str)->None:
#     if name not in NAMES:
#         return
#
#     size = 5
#     def square_shape() -> None:
#         global size
#         size = 6
#         for i in range(size):
#             for j in range(size):
#                 print('*', end=' ')
#             print()
#
#
#     def rectangle_shape() -> None:
#         for i in range(size):
#             for j in range(size*2):
#                 print('*', end=' ')
#             print()
#
#     if name == 'square':
#         square_shape()
#     elif name == 'rectangle':
#         rectangle_shape()
#
# # geometric_shape(name='square')
# # geometric_shape(name='rectangle')
# print(size)
import random


# classwork
# Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі діапазону передаються як параметри. Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.
# Створити окремо функцію яка повертає в нижню і верхню межу в коректному порядку.
# доповнити попередню функцію щоб вказаний діапазон заповнювався випадковими числами, після отриманий список чисел використовується для отримання добутку чисел.
# import random
#неправильно выполненное задание
# start = int(input('enter start value: '))
# end = int(input('enter end value: '))
# length = int(input('enter a length on list: '))
# def correct_diapason(a=start, b=end):
#     diapason_list = []
#     c = 0
#     if length >1:
#         if a > b:
#             c = b
#             b = a
#             a = c
#     for i in range(length):
#         diapason_list.append(random.randint(start,end))
#     return diapason_list
#
# def multiply_frome_range():
#     multy =1
#     new_list = correct_diapason()
#     for i in new_list:
#         multy = multy*i
#     return multy
#
# print(multiply_frome_range())

def check_diapason(a, b):
    if b > a:
        return a,b
    else:
        return b, a

def multy_in_diapason(c, e):
    c,e  = check_diapason(c,e)
    multy = 1
    for i in range(c,e+1):
        multy = multy*i
    return multy

start = random.randint(1,20)
end = random.randint(1,20)

start, end = check_diapason(start, end)
print(start,end)
print(multy_in_diapason(start, end))