#To Calcculate the Roots for Quadratic Equation

import cmath

num1 = int(input("Enter the first number:"))#Take three numbers from user as num1,num2,num3
num2 = int(input("Enter the Second number:"))
num3 = int(input("Enter the Third number:"))


def Quadratic(num1, num2, num3):#Defining function
    delta = (num2 ** 2) - (4 * num1 * num3)#Calculating delta by using formula
    Root1 = (-num2 + cmath.sqrt(delta)) / (2 * num1)#Calculating Root1 and Root2 for three numbers
    Root2 = (-num2 - cmath.sqrt(delta)) / (2 * num1)
    print('The Roots are {0} and {1}'.format(Root1, Root2))#Display the result by Using format function to calculating the complex numbers


Quadratic(num1, num2, num3)
