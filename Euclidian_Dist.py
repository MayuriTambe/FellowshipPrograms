#To calculate the Euclidean Distance

import math #importing math function

FirstNumber=int(input("Enter First number:"))#Take two numbers from user
SecondNumber=int(input("Enter Second number:"))

def EuclidianDist(FirstNumber,SecondNumber):#Defining Function
    point_x = math.pow(FirstNumber, 2)#By using math function find the values
    point_y = math.pow(SecondNumber,2)

    result=math.sqrt(point_x + point_y)#Calculate the distance Of two co-ordinates
    print('The Distance is=',result)#Print the Result

EuclidianDist(FirstNumber,SecondNumber)
