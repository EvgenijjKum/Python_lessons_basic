
__author__ = 'Кумпяков Евгений'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
print("Задача 1")

loop = True
while loop:
    number = input('Ведите произвольное целое число:\n')
    if number.isdigit():
        loop = False
    else:
        print('Некорректный ввод!')

var_temp = list(number)

for i in var_temp:
    print(i)

print("Конец Задачи 1")
print()



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print("Задача 2")

loop = True
while loop:
    number_a = input('Ведите произвольное целое число a:\n')
    if number_a.isdigit():
        loop = False
    else:
        print('Некорректный ввод!')

loop = True
while loop:
    number_b = input('Ведите произвольное целое число b:\n')
    if number_b.isdigit():
        loop = False
    else:
        print('Некорректный ввод!')

print('Исходный ввод: число a = ', number_a)
print('Исходный ввод: число b = ', number_b)

number_temp = number_a
number_a = number_b
number_b = number_temp

print('Вывод после замены: число a = ', number_a)
print('Вывод после замены: число b = ', number_b)

print("Конец Задачи 2")
print()


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print("Задача 3")

loop = True
while loop:
    number = input('Ведите число полных лет своего возраста:\n')
    if number_a.isdigit():
        loop = False
    else:
        print('Некорректный ввод!')

if int(number) < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")

print("Конец Задачи 3")
print()
