#Print the year Leap year or not

year=int(input("Enter the year")) #Take input from user

def LeapYear():#Defining function LeapYear

    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))): #if the year is divisible 400 OR year is divisible by 4
        # but not divisible by 100
        print("This is leap year")  # if condition is true then print leap year
    else:
        print("This is not leap year")  # if condition is false then print not leap year


print(LeapYear())