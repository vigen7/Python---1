# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number*(10**ndigits) + 0.5
    number = number//1
    return number / (10 ** ndigits)
number = my_round(2.1234567, 5)
print(number)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    t1 = ticket_number_str[:3]
    t2 = ticket_number_str[3:]
    sum1 = 0
    for a in t1 :
        sum1 = sum1 + int(a)
    sum2 = 0
    for a in t2 :
        sum2 = sum2 + int(a)
    if sum1 == sum2 :
        res_mes = "Победа"
    else:
        res_mes = 'В следующий раз'
    return res_mes
res = lucky_ticket(444444)
print(res)

