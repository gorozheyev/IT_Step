
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


print("Ваши задачи на день")

while True:

    action = input("Выберете опцию для дальнейшего действия:\n"
                   "1 - добавить задачу\n"
                   "2 - просмотреть задачи\n"
                   "0 - выйти из приложения\n"
                   "- ")

    if action == "0":
        print("Программа завершена")
        break

    if action == "1":
        with open("tasks.txt", "a") as file:
            new_task = input("Введите задачу:\n")
            file.write(new_task + "\n")
            print("Задача добавлена в список\n")

    elif action == "2":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readline()
                print("Список ваших задач:")
                while tasks:
                    print(tasks, end="")
                    tasks = file.readline()
                print()
        except FileNotFoundError:
            print("Список задач пуст")


    else:
        print("Неверный ввод выберите 0, 1 или 2")
