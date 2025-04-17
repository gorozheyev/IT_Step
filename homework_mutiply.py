# вывод простых чисел
# start = int(input('enter start value: '))
# end = int(input('enter end value: '))
#
# if start < end and start > 1:
#     for n in range(start, end + 1):
#             for i in range(2, int(n ** 0.5) + 1):  # Перевіряємо дільники до √n
#                 if n % i == 0:
#                     break
#             else:
#                 print(n, end=" ")  # Виводимо число в один рядок
# else:
#     print('please enter correct range')

first = int(input('enter start value: '))
second = int(input('enter end value: '))
for i in range(first, second +1):
    for j in range(1, 11):
        print(i, '*', j, '=', i*j, end=' | ')
    print()