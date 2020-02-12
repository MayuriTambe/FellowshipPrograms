#Print the String with Username

str="Hello <<username>>,how are you?"#Take a string
name=input("Enter your name : ")

def ReplaceString(str,name):#Defining function
   Result= str.replace("<<username>>", name)#Using string replace function to replace string.
   print("The Replace String is=",Result)#Display the result

ReplaceString(str,name )



