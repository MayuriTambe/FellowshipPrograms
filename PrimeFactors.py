n=int(input("Enter an integer:"))#Take number from user

def PrimeFactors(n):#Define Function
    i=1#Initialize the i variable
    while (i <= n):#Travesing using While loop
        count = 0#Initialize the count=0
        if (n % i == 0):#If number is divisible by i then assign j=1,else out if the loop
            j = 1
            while (j <= i):#Checking Condition
                if (i % j == 0):
                    count = count + 1#Increment count
                j = j + 1
            if (count == 2):#if count==2 then print Result
                print(i)
        i = i + 1

PrimeFactors(n)