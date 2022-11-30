# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

number = int(input('Enter number from 1 to 7: '))
if 0 < number < 6:
    print('Weekday')
elif number == 6 or number == 7:
    print('Weekend')
else:
    print('Incorrect number')

