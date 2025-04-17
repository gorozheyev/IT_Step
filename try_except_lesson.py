
# string = input("Input nums: ")
# number= int(string)
# print(number)


# try:
#     ergpoiogj[pqetrihjo'
#         'qknhtrpl;oqirjkthqwrth'
# except:
#     rfothjortpijhoijrthopij



# try:
#     number = int(input("Input nums: "))
#     print("Введенное число: ",number)
# except:
#     print("Преобразование прошло неудачно")
# print("Task complited")


#try:
#     number = 3/0
#     print(number)
# finally:
#     print("Блок try завершил выполнение")
# print("Task complited")


# try:
#     number = int(input("Input nums: "))
#     print("Введенное число: ",number)
# except ValueError:
#     print("Преобразование прошло неудачно")
# print("Task complited")



# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Result: ", number1/number2)
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except BaseException:
#     print("Общее исключение")
# print("Task complited")


# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Result: ", number1/number2)
# except (ValueError,ZeroDivisionError) :
#     print("Попытка деления на 0 или некорректный ввод")
#
# print("Task complited")



try:
    age = int(input("Введите возраст: "))
    if age > 100 or age < 1:
        raise Exception("Некорректный возраст")
    print("Ваш возраст: ", age)
except ValueError:
    print("Преобразование прошло неудачно")
except Exception as e:
    print(e)
print("Task complited")