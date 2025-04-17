# функция выводит ткст
# def print_text():
#     str = '"Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself."\nBill Gates'
#     return print(str)
#
# print_text()

# функция выводит парные числа в диапазоне
# def even_numbers(a, b):
#     for i in range(a,b+1):
#         if i%2 == 0:
#             print(i, end=' ')
#     return 0
#
# even_numbers(4,30)

#функция рисует заполненный или пустой квадрат
# def show_square(side, symbol, boolean):
#     if boolean:
#         for i in range(side):
#             for j in range(side):
#                 print('*', end=' ')
#             print()
#     elif not boolean:
#             for k in range(side):
#                 for n in range(side):
#                     if k ==0 or k == side-1  or n == 0 or n == side-1:
#                         print(symbol, end=' ')
#                     else:
#                         print(' ', end=' ')
#                 print()
#
# show_square(7, '*', True)

# минумум из 5 чисел
# def min_from_values(num1, num2, num3, num4, num5):
#     list = [num1, num2, num3, num4, num5]
#     return min(list)
#
# print(min_from_values(-444.9, 50,5, -100,0))

#произведение чисел из диапазона
# def multy_from_list(a, b):
#     multy = 1
#     for i in range(a, b+1):
#         multy = multy*i
#     return multy
#
# print(multy_from_list(2,5))

# количекство цифр в числе
# def count_numbers(number: str):
#     count = 0
#     number_new = str(number)
#     for i in number_new:
#         count = count + 1
#     return count
#
# print(count_numbers(34543288))

# проверка числа на полиндромность
def polindrom_number(a):
    value = str(a)
    reversed_value = value[::-1]
    if value ==reversed_value:
        return True
    else:
        return False

print(polindrom_number(123312))