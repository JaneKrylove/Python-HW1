# 3.	Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

a = int(input('Input coordinate x: '))
b = int(input('Input coordinate y: '))

if a == 0 or b == 0:
    print('This point is on the line')

elif a > 0 and b > 0:
    print('This quarter is 1')
elif a < 0 and b > 0:
    print('This quarter is 2')
elif a < 0 and b < 0:
    print('This quarter is 3')
else:
    print('This quarter is 4')


