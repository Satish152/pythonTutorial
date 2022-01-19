# The filter() method filters the given sequence with the help of a function that tests each element
# in the sequence to be true or not.

#it accepts two arguments, one is function which returns the output and one is iterator like list
lst=[1,3,4,6,8,7,9]

s=list(filter(lambda a:a%2==0,lst))

print(s)

# map() function returns a map object(which is an iterator) of the results after applying the given
# function to each item of a given iterable (list, tuple etc.)

sum=list(map(lambda a:a*2,s))
print(sum)

# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of
# the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
from functools import  *
result=reduce(lambda  a,b:a+b,sum)

print(result)
