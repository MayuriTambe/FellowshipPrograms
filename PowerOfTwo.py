#Print the Power Of two for nth Number

import math #importing math function

number = int(input("Enter the number:"))#Take  number from user

def PowerOfTwo(number):#Defining Function
    power = 0#Initialize the power
    i=0

    if number <= 31:#Checking condition
        for i in range(0, number):#Iterating from 0 to number
            power = math.pow(2, i)#Calculating the power by using Pow function
            i+=1#Incrementing i

    print(power)#Display the Result


PowerOfTwo(number)
