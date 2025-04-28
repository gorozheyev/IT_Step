import os


#mkdir() - создает новую папку
#rmdir() - удаляет папку
#rename() - переименовывает файл
#remove() - удаляет файл



# os.mkdir("hello")
#os.mkdir("c://somedir")

# os.rmdir("hello")
# os.rmdir("c://somedir")


# os.rename("hello.txt", "hello2.txt")


# filename = input("Введите путь к файлу: ")
# if os.path.exists(filename):
#     print("Указаный файл существует")
# else:
#     print("Файл не существует")



# classwork print tree by path
# def print_tree(start_path):
#     for root,dirs,files in os.walk(start_path):
#         level = root.replace(start_path,"").count(os.sep)
#         indent = "|  " * level
#         folder_name = os.path.basename(root)
#         print(f"{indent}|--{folder_name}")
#
#
#         for f in files:
#             print(f"{indent}|  |--{f}")
#
#
# path = input("Введите путь к папке: ")
# print(f"Сканирование папки: {path}\n")
# print_tree(path)



# переделанный запуск программы через рекурсию, начата на уроке и закончена дома
def print_tree(path, level = 0):
    indent = "|  " * level
    try:
        folder_name = os.path.basename(path)
        print(f"{indent}|--{folder_name}")

        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print_tree(full_path, level + 1)
            else:
                print(f"{indent}|  |--{item}")
    except PermissionError:
        print(f"{indent} Permission denied: {path}")
    except Exception as e:
        print(f"{indent}️ Error accessing {path}: {e}")

start_path = input("ввелите путь к файлу или / для сканирования от корня: ")  # Сканируем с корня
print(f"Сканирование всего диска, начиная с корня или введенного пути: {start_path}\n")
print_tree(start_path)
