# when we want to use a global variable inside any function, we should need to use keywoerd called global
# which helps to treat that variable as a global variable which is already defined outside
# if we want to use a global variable with out defining it as global inside of function, it consider it as a new variable
# globals() is a function which returns all the global variables defined outside fo the code and we can ab;e to
# access thpse  global variables using this function

# note : once we define a variable name as global inside of function, we can't able to create a new local variable
# with same name like global variable

a=10
def age():
    global  a #here we told to the function like this 'a' is a global variable
    a=15

age()
print(a)

# now we want to access global variables using globals() function

def name():
    a=20  #this a is now consider as a local variable and it won't change the valud og Global a
    x= globals()['a'] # here we assigning global a value in to X
    print(a)
    print(x)
    #and if we want to update global value, we can't directly change the x value, it will consider as a new variable
    globals()['a']=35 #by directly using globals function we can update the value
    
name()
print(a) #trying to print the global value to check whether the a value is updated or still same