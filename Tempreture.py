celsius=int(input("Enter the Tempreture in Celsius:"))#Take Tempreture in Celsius from user
fahrenheit=int(input("Enter the tempreture in fahrenheit"))#Take Tempreture in fahrenheit from user


def Countcelsius():#Declaring function
    celsius = (fahrenheit - 32) * 5 / 9#Coverting Temprture into Celsius by using formula
    print("Temperatur in Celsius ",celsius)#Display Result

Countcelsius()
def Countfahrenheit():#Declaring function
    fahrenheit=(celsius * 9 / 5) + 32;#Converting Tempreture into fahrenheit by using formula
    print("Temperature in fahrenheit ",fahrenheit)#Display Result
Countfahrenheit()