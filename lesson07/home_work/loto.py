#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

def str_card_pos():
    # На выходе функции получем матрицу для расстановки чисел:
    # например: [1, 0, 1, 0, 0, 0, 1, 1, 1]
    str_card = [0 for i in range(9)]      # создаем список, заполняем его "нулями"
    # если количество едениц в ряду меньше 5, "дописываем" в случайные места еденицы
    loop = True
    while loop:
        count_num = 0
        pos = random.randint(0,8)
        str_card[pos] = 1
        for x in str_card:
            if x:
                count_num +=1
        if count_num == 5:
            loop = False
    return str_card

def card_init():
    # создаем список цифр используемых в карте: 3 стороки * 5 цифр = 1 карточка
    number_all_for_card = []
    for i in range(15):                                 # заполняем список
        loop = True
        while loop:
            number = random.randint(1, 90)
            if number not in number_all_for_card:       # заполняем список только уникальными числами
                number_all_for_card.append(number)
                loop = False
    arr_0 = number_all_for_card[:5]
    arr_1 = number_all_for_card[5:10]
    arr_2 = number_all_for_card[10:]
    arr_0.sort()
    arr_1.sort()
    arr_2.sort()
    number_all_for_card = arr_0 + arr_1 +arr_2
    card = [[], [], []]
    card_matrix = [str_card_pos(), str_card_pos(), str_card_pos()]

    count_num = 0
    for i in range(0, 3):
        for j in range(0, 9):
            if card_matrix[i][j]:
                card[i].append(number_all_for_card[count_num])
                count_num += 1
            else:
                card[i].append(0)
    return card

#   Выводим красивую строку (вместо "0" пробелы), вида "20 49    56 81       83  "
def print_str(my_str):
    str_out = ''
    for i in my_str:
        if i > 0:
            str_out += str(i).rjust(2)
        elif i < 0:
            str_out += ' -'
        else:
            str_out += '  '
        str_out += ' '
    print(str_out)

#-----------------------------------------------
class Loto_Card():
    def __init__(self, name):
        self.name = name
        self.card = card_init()
        self.score = 0

    def show_card(self):
        if self.name == 'user':
            print('------ Ваша карточка -----')
        else:
            print('-- Карточка компьютера ---')
        #print('--------------------------')
        print_str(self.card[0])
        print_str(self.card[1])
        print_str(self.card[2])
        print('--------------------------')

    def del_number(self,number):
        not_correct_num = 1
        for i in range(0, 3):
            for j in range(0, 9):
                if self.card[i][j] == number:
                    self.card[i][j] = -1
                    not_correct_num = 0
                    self.score += 1
                    return 0
        if not_correct_num:
            if self.name == 'user':
                print('Числа ' + str(number) + ' нет на карточке')
                return 1
        return 0

#-----------------------------------------------
def show_barrel(used_barrel):
    loop = True
    while loop:
        num_barrel = random.randint(1, 90)
        if num_barrel not in used_barrel:  # заполняем список только уникальными числами
            used_barrel.append(num_barrel)
            loop = False
    print('--------------------------')
    print('Новый бочонок: ' + str(num_barrel) + ' (осталось ' + str(90 - len(used_barrel)) + ')')
    return num_barrel


#--------------Основной блок--------------------------------
print('                   Приветствую!')
print('                  Игра ==ЛОТО==')
print('----------------------------------------------------')
with open(r"loto_pravila.txt", "r") as f:
    arr = f.readlines()
    for i in arr:
        print(i, end='')
print()

card1 = Loto_Card('user')
card2 = Loto_Card('comp')

used_barrel = []
correct_input = 1

loop = True
while loop:
    if correct_input:
        new_barrel = show_barrel(used_barrel)
        card1.show_card()
        card2.show_card()

    com_input = input('Зачеркнуть цифру? (y/n) \n')
    if com_input == 'y':
        correct_input = 1
        if card1.del_number(new_barrel):
            print('---------Вы проиграли!---------')
            loop = False
            break

    elif com_input == 'n':
        correct_input = 1
        if card1.del_number(new_barrel) == False:
            print('Вы не зачеркнули на карточке число: ' + str(new_barrel))
            print('---------Вы проиграли!---------')
            loop = False
            break

    elif com_input == 'exit':
        correct_input = 1
        print('Введена команда прерывания игры')
        loop = False
        break
    else:
        print('Введена неопределенная команда')
        print('-------Повторите ввод!--------')
        correct_input = 0

    card2.del_number(new_barrel)
    if card1.score == 15:
        print('---------Вы победили!----------')
        loop = False
        break
    elif card2.score == 15:
        print('---------Вы проиграли!---------')
        loop = False
        break

print('---------До свидания!----------')
