#Given Tempreture and Speed calculate the windChill using Formula

import math#Importing math function
Tempreture=int(input("Enter the Tempreture: "))#Take Tempreture and Speed as input
Speed=int(input("Enter the Speed: "))


def WindChill(Tempreture,Speed):#Defining function
    if Tempreture< 50 and Speed < 120 :#Checking the condition
        Wind=math.pow(Speed, 0.16)#Calculating wind using math.pow function
        WindChill=35.74 + (0.6215 * Tempreture) + ((0.4275 * Tempreture) - 35.75) * Wind#USing formula for Windchill
        print(WindChill)#Display result
    else:
        print("Invalid")#if condition false print Invalid


WindChill(Tempreture, Speed)

