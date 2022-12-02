# 5.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве.

x1 = float(input('Enter the first coordinate of A point: '))
y1 = float(input('Enter the second coordinate of A point: '))

x2 = float(input('Enter the first coordinate of B point: '))
y2 = float(input('Enter the first coordinate of B point: '))

lengthAB = ((x2 - x1) + (y2 - y1))**0.5

print(round(lengthAB, 2))