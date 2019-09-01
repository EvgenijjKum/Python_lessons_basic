# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#---------Решение--------------------
# скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
import os
import sys
import shutil
import re

for i in range(1,10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))

a = input("нажмите Enter, для продолжения")

#скрипт, удаляющий папки dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.

for i in range(1,10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Директория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('Директория {} не найдена'.format(dir_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


my_dir_list = os.listdir()

dir_no_find = 1

for i in my_dir_list:
	if os.path.isdir(i):
		print('Папка: ' + '/' + i)
		dir_no_find = 0

if dir_no_find:
	print('В текущей директории папок не найдено')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


a = re.compile(r"[a-z0-9_]+")
str_name = a.findall(sys.argv[0])

file_copy_name = str_name[0] + '_copy' + '.'+ str_name[1]

shutil.copy(sys.argv[0],file_copy_name)


