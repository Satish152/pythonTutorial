#numpy is a module which is available in python helps to deal with arrays and matrixes
#in a normal array module there is no way to create multi dimensional array, to overcome that we ca use this numPY

from numpy import *
arr=array([
[1,2,3],
[4,5,6]
])

print(arr)

#above array format return the two dimensional array

print(arr.dtype) #prints the array data type
print(arr.shape) #returns the rows anf col
print(arr.ndim) #returns the dimension of array


print(arr.flatten()) #it turns the array in to one dim array
arr2=arr.flatten()
print(arr2.reshape(3,2)) #it converts the one dim array to 3row,2col 2dim array

#when we copying the array by using arr1=arr2 , both arr1 and arr2 shares same id and if any one array got change
#in data, automatically second array also got impacted


print("copying the array using = , both arr and arr2 sharing same id")
arr2=arr
print(id(arr2))
print(id(arr))

print("copying the array using view(), both arr and arr2 sharing same id")
arr2=arr.view()
print(id(arr2))
print(id(arr))

arr=array([
[1,2,3],
[4,5,7]
])

print(arr)
print(arr2)

print("by using this Copy() function , arr and arr2 will have the different arr id")
arr2=arr.copy()
print(id(arr))
print(id(arr2))

