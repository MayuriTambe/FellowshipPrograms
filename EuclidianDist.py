#To calculate the Euclidean Distance

import math #importing math function

number1=int(input("Enter First number:"))#Take two numbers from user
number2=int(input("Enter Second number:"))

def EuclidianDist(number1,number2):#Defining Function
    xx = math.pow(number1, 2)#By using math function find the values
    yy = math.pow(number2,2)

    result=math.sqrt(xx+yy)#Calculate the distance Of two co-ordinates
    print('The Distance is=',result)#Print the Result

EuclidianDist(number1,number2)
