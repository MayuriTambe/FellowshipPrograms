#To find the Triplets whose sum is equal to zero.

array=[1, -1, 2, 0, -2, 4, -2, -2, 4]#Declare an Array
n=len(array)#Initialize the length of Array
def ThreeNums(array,n):#Defining Function
    for i in range(0, n):#Iterating for first Element in list
        x=array[i]#Stroring the Element in x variable

        for j in range(i+1, n):#Iterating for Second Element in list
            y=array[j]#Storing the Element in y Variable

            for k in range(j+1, n):#Iterating for Third Element in list
                z=array[k]#Storing the Element in z Variable

                if (x+y+z==0):#If addition of three Numbers is 0 then print the Elements
                    print(x,y,z)

ThreeNums(array,n)



