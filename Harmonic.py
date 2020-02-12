#Print the nth Harmonic Values

number=int(input("Enter the number"))##Take a number from user

def Harmonic(number):#Defining Function
    HarmonicNumber=1.0#Initialize the value

    for i in range(2, number):# Iterating each number in list
        HarmonicNumber += 1 / i#Calculating the Harmonic Number
    print(HarmonicNumber)#Print the Result

Harmonic(number)