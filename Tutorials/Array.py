#Arrays in python is need import of Array function  from array modules
#it accepts the array type, and list of values

#in array function we need to pass two arguments, 1 is typecode and 2 is array datsa
# i is signed int which starts from negative to positive
# I is unsigned int which won't accept negativevalue.. when we use negative value it gives "Can't convert negative
# values in unsigned integer
# not only for integer, same for short,byte,long,double data types have signed and unsigned 
from array import *
arr=array("i",[1,2,3,4,-5])

for i in arr:
    print(i)


newArr=array(arr.typecode,(a+2 for a in arr))

for num in newArr:
    print(num,end=" ")

#like java it doesn't need define size before array creation and also we can add values even after array creation

arr=array('i',[]) #creating empty array
size=int(input("Enter the array size : "))
for i in range(size):
    arr.append(int(input("Enter the value : ")))

print(arr," created array")

#in run time added 26 to the array
print(arr.append(26),arr)