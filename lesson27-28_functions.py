print('Lesson 27-28 list pointer, function\n')

# def some_function():
#     pass

# function without parameters
# def show_square():
#     a = 5
#     b = 6
#     for i in range(a):
#         for j in range(b):
#             print('*', end=' ')
#         print()
#
# show_square()

# function with parameters
# def show_square(a: int, b: int):
#     for i in range(a):
#         for j in range(b):
#             print('*', end=' ')
#         print()
#
# width = 4
# height = int('5')
# show_square(width, height)

# function with default parameters
# def show_square(a: int, b: int, space = ' ', symbol='*'):
#     for i in range(a):
#         for j in range(b):
#             print(symbol, end=space)
#         print()
#
# width = 4
# height = int('5')
# show_square(width, height, symbol='x', space='-')

# function with return result
# def show_square(a: int, b: int, space = ' ')->int:
#     if a < 2 or b <2:
#         print('value is < 2')
#         return 0
#
#     sum_value = 0
#
#     for i in range(a):
#         for j in range(b):
#             print(i+j, end=space)
#             sum_value += (i+j)
#         print()
#
#     return sum_value
#
# width = 4
# height = int('2')
# result = show_square(width, height, space='\t')
# print(f'{width}x{height} = {result}')

# function with *args
# def get_weight_figure(width: int, height: int, length: int, density: float)->float:
#     pass

# def get_weight_figure(*args)->float:
#     return args[0]*args[1]*args[2]*args[3]
#
# print(get_weight_figure(1,2,3,4))

# ---------------------------

# classwork
def value_to_int(value = 'enter a vallue: '):
    for i in range(3):
        user_input = input(value)
        user_input = user_input.strip().replace('-','')
        if user_input.isdigit():
            return int(user_input)
        print('enterr value one more time')
    print('all attempts used')
    return 0

number = value_to_int()
print(f'value converted to ABS INT = {number}')

def squear_from_number(number: int, space = '\t'):
    if number > 1:
        for i in range(number):
            for j in range(number):
                    print(i*j, end=space)
            print()
    else:
        print('value should be grater than 1')
        return 0

squear_from_number(number)

