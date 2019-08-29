# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    my_number = str(number)
    pos = my_number.find('.') + ndigits +1
    znak = int(my_number[pos]) #нашли знак для отбрасывания
    if znak >=5:
        mod = 1
    else:
        mod = 0
    my_number = float(my_number[:pos])
    
    var_result = '0.'
    for i in range(ndigits-1):
        var_result += '0'

    var_result += str(mod)# число-модификатор
    var_result = float(var_result) + my_number

    return var_result



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    my_tiket_number = str(ticket_number)
    if len(my_tiket_number) !=6:
        return 'Ошибка введенного номера'
 
    str_low  = my_tiket_number[:3]
    str_hi = my_tiket_number[-3:]
    
    res_low = 0
    res_hi = 0
    for x in str_low:
        res_low += int(x)
    for x in str_hi:
        res_hi += int(x)
    
    if res_low == res_hi:
    	return 'Счастливый билет!'
    else:
    	return 'Билет не является счастливым'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
