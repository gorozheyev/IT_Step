from math import degrees

print('Lesson 31-32 recursion, lambda, closure function \n')

# temp_arr = ['folder1', ['sub_folder1', ['under_sub_folder1', ['file1'], 'under_sub_folder2'], 'sub_folder2'], 'folder2']

# recursion function
# def factorial(n:int)->int:
#
#     # call guidance
#     if n == 1:
#         return 1
#
#     return n * factorial(n-1)
#
# number = 6
#
# print('result', factorial(number))

# def sum_value(a: int, b: int)->None:
#     print(f'{a} + {b} = {a+b}')
#
# def sum_multiply(a: int, b: int)->None:
#     print(f'{a} x {b} = {a*b}')

# sum_value(3, 2)
# sum_multiply(3, 2)

# arr_functions = [sum_value, sum_multiply]
# arr_functions[0](4, 6)

# call_function = lambda : print('lamda function called')
# call_function()

# call_sum = lambda a, b: print(f'{a} + {b} = {a + b}')
# call_sum(2, 5)

# def get_sum_value(a: int, b: int)->int:
#     return a + b
#
# get_sum = lambda a, b: (a + b)**2
# print(get_sum(2,5))

# closure function

# def set_circle_square(scalar: float):
#
#     def get_square(r: float) -> float:
#         return scalar * r**2
#
#     return get_square
#
# circle_square = set_circle_square(3.14)
#
# square = circle_square(2)
# print(square)

# classwork возведение числа в степень
# def pow_function(exp: float):
#
#     def do_pow(value: float) -> float:
#         return value**exp
#     return do_pow
#
# degree = int(input('введите степень: '))
# power = pow_function(degree)
#
# number = int(input('введите число: '))
# result = power(number)
#
# print(f'{number} в стеаени {degree} = ', result)


# Написати рекурсивну функцію знаходження степеня числа.
# def number_in_exp(number:float, exp: int)->float:
#
#     # call guidance
#     if exp == 0:
#         return 1
#     elif exp <0:
#         return 1/number_in_exp(number, -exp)
#     else:
#         return number * number_in_exp(number, exp -1)
#
# number = float(input('enter a value: '))
# exp = int(input('enter an exponent: '))
#
# print(f'{number} in exponent {exp} =', number_in_exp(number, exp))

# За допомогою рекурсії перевірити, чи є слово паліндромом (тобто читається у прямому та зворотному
# напрямку однаково, наприклад, слово «мадам» — паліндром).
# def polindrom_recursion(text: str):
#     if len(text) <= 1:
#         return True
#     elif text[0] == text[-1]:
#         return polindrom_recursion(text[1:-1])
#     else:
#         return False
#
# word = input('Enter a polindrom word: ').lower().strip()
#
# if polindrom_recursion(word):
#     print(f'{word} - is polinrom')
# else:
#     print(f'{word} is not a polindrom')

# створити 4 лямбда функції які виконують основні арифметичні операції:- додавання,- віднімання,- множення,- ділення
# всі 4 - лямбда функції передати до списку та викликати через цикл відобразивши результат кожної арифметичної операції.
call_sum = lambda a, b: print(f'{a} + {b} = {a + b}')
call_min = lambda a, b: print(f'{a} - {b} = {a - b}')
call_multy = lambda a, b: print(f'{a} * {b} = {a * b}')
call_devision = lambda a, b: print(f'{a} / {b} = {a / b}')

list = [call_sum, call_min, call_devision, call_multy ]

def operation_math(a, b):
    for operation in list:
        if operation == call_devision and b ==0:
            print('devision by zero')
            continue
        operation(a, b)

number1 = float(input('enter the first value:'))
number2 = float(input('enter the second value:'))

operation_math(number1, number2)

