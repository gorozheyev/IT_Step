
#open(file,mode)
#r(read)
#w(write)
#a(append)
#b(binary)
#r+(r+a)

# myfile = open("hello.txt", "w")
#
# myfile.close()


#
# try:
#     myfile = open("hello.txt", "w")
#     try:
#         print("работа с файлом")
#     finally:
#         myfile.close()
# except Exception as ex:
#     print(ex)



#
# with open(file,mode) as myfile:
#     инструкция


# with open("hello.txt", 'w') as myfile:
#     print("Работа с файлом")



# with open("hello.txt", 'a') as myfile:
#     myfile.write("\nhello work")
#
# print("Файл изменен")


# lines = ["Apple\n", "Pen\n", "Applepen\n"]
#
# with open("hello.txt", 'w') as myfile:
#     myfile.writelines(lines)
#
# print("Файл изменен")

#
# with open("hello.txt", "r") as file:
#     for line in file:
#         print(line, end="")



# with open("hello.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()


# with open("hello.txt", "w+") as file:
#     file.write("Hello world\n")
#     file.seek(6)
#     content = file.read()
#     print(content)

from datetime import datetime, date


def is_valid_date(date_str: str, date_format: str = "%d.%m.%Y") -> bool:
    """
    Проверяет, соответствует ли строка date_str формату date_format.
    По умолчанию формат "%d.%m.%Y" (день.месяц.год).
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


print("Ваши задачи на день")

while True:

    action = input("Выберете опцию для дальнейшего действия:\n"
                   "1 - добавить задачу\n"
                   "2 - просмотреть задачи\n"
                   "3 - введите задачу с дедлайном\n"
                   "0 - выйти из приложения\n"
                   "Ваш выбор: ")

    if action == "0":
        print("Программа завершена")
        break

    if action == "1":
        with open("tasks.txt", "a") as file:
            new_task = input("\nВведите задачу:\n")
            file.write(new_task + "\n")
            print("Задача добавлена в список\n")

    elif action == "2":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readline()
                print("\nСписок ваших задач:")
                while tasks:
                    print(tasks, end="")
                    tasks = file.readline()
                print()
        except FileNotFoundError:
            print("Список задач пуст")

    elif action == "3":
        with open("tasks.txt", "a") as file:
            new_task = input("\nВведите задачу:\n")
            file.write(new_task + " ")
            dedline = input("введите дедлайн в формате ДД-ММ-ГГГГ: ")
            if is_valid_date(dedline):
                file.write(dedline + " ")
                done = int(input("Выберите статус:\n"
                             "1 - выполнена\n"
                             "0 - не выполнена\n"
                             ": "))
                if done == 1:
                    file.write("[Task completed]\n")
                    print("Задача с дедлайном добавлена в список\n")
                elif done == 0:
                    file.write("[Task is not completed]\n")
                    print("Задача с дедлайном добавлена в список\n")
                else:
                    print("Выберите статус 1 или 2")

            else:
                print("Введите дату в правильном формате")

    else:
        print("Неверный ввод выберите 0, 1 или 2")
