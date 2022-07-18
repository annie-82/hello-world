'''
Name = Sunhwa Nam
Date : Oct 25, 2021
The following programs are for the Lab5 activity
'''

#Problem 1: This program prints Hello World 100 times.
for i in range (1, 101):
   print("Hello World")

'''Problem 2 – Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20.
a.Write a loop that prints each of the numbers on a new line.
'''
numList = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in numList:
    print(i)

'''b.Write a loop that prints each number and its square on a new line'''
for i in numList:
    print("{} and its square value is {}".format(i, i**2))

'''Problem 3 – Write a program that asks the user for the number of sides, 
the length of the side, the color of the line, and the fill color of a regular polygon.
 The program should draw the polygon and then fill it in'''
#if there is number of sides, the angles are generated.'''

import turtle
wn = turtle.Screen()
t = turtle.Turtle()
penColor = input("Enter for the color of sides")
#set a color of the pen
t.color(penColor)

noSide = int(input("Enter the number of sides"))
length = int(input("Enter the length of each side"))
fillColor = input("What color do you want to fill the polygon")

t.fillcolor(fillColor)
t.begin_fill()
for i in range(noSide):
    t.forward(length)
    t.left(360/noSide)

t.end_fill()

wn.exitonclick()

