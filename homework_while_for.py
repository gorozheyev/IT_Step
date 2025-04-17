# a = int(input('enter first value: '))
# b = int(input('enter second value: '))
# count_even = 0
# sum_even = 0
# sum_odd =0
# count_odd = 0
# sum_equal9 = 0
# count_equal9 = 0
# if a < b:
#     while a <= b:
#         if a%2 == 0:
#             sum_even = sum_even + a
#             count_even = count_even + 1
#             # print(sum_even)
#             # print(count_even)
#         else:
#             sum_odd = sum_odd + a
#             count_odd = count_odd + 1
#
#         if a%9 ==0:
#             sum_equal9 = sum_equal9 + a
#             count_equal9 = count_equal9 + 1
#         a = a + 1
#     avg_even = sum_even/count_even
#     avg_odd = sum_odd/count_odd
#     avg_equal9 = sum_equal9/count_equal9
#
#     print(f'сумма четных = {sum_even} , среднее арифметическое = {avg_even}')
#     print(f'сумма нечетных = {sum_odd} , среднее арифметическое = {avg_odd}')
#     print(f'сумма кратных 9 = {sum_equal9} , среднее арифметическое = {avg_equal9}')
#
# else:
#     print('введенный диапазон не корректный')

# -----------------------------------

# sum = 0
# min = 12313133
# max_value = -12313133
# while True:
#     value = int(input('введите число: '))
#     if value != 7:
#         sum = sum + value
#         if value < min:
#             min = value
#         if value > max_value:
#             max_value = value
#     else:
#         print('Good bye')
#         print(sum)
#         print(min)
#         print(max_value)
#         break


# string = 'phhyyyttttooooonnnnnn'
# new_string = ''
# for i in string:
#     if i not in new_string:
#         new_string +=i
# print(new_string)

value = int(input('enter a size of squear: '))
for i in range(value):
    for j in range(value):
        if i==0 or i == value-1 or j ==0 or j == value-1 or j <= i and j < (value - i) or j >= i and j >= (value -1 - i):
            print('*', ' ', end='')
        else:
            print(' ', ' ', end='')
    print()

# value = int(input('enter a size of squear: '))
# for i in range(value ):
#     for j in range(value):
#         if j <= i and j < (value - i) or j >= i and j >= (value -1 - i):
#             print('*', ' ', end='')
#         else:
#             print(' ', ' ', end='')
#     print()