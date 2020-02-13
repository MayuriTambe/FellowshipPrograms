#Flip coin and calculate heads and tails percentage

import random#Importing Random function to randomly flip coin

def FlipCoin():#Defining flipcoin Function
    no_chances = int(input("Enter the no of chances:"))#Take number of chances from user
    Head=0#Initializing
    tails=0
    flip=1
    while flip<=no_chances:#checking condition
        if random.randint(0,1):#Using Random.randint function to calculate Possibilties
            Head=+1#Incrementing head
        else:#If condition is false then
            tails+=1#Incrementing Tails
        flip+=1
    print("HeadPercentage=",(Head*100)/no_chances)#Display HeadPercentage
    print("TailsPercentage=",(tails*100)/no_chances)#Display TailsPercentage
FlipCoin()


