#Print the String with Username
import re#Importing Regex
String=input("Enter the String to Replace:")#Take a string

str = "Hello <<UserName>>, How are you?"

def Replace():#Defining function
   ReplaceString = re.sub("<<\w+>>", String, str)#Using string replace function to replace string.
   print(ReplaceString)#Display the result

Replace()

