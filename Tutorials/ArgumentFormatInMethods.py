#In a function, to pass the arguments, we have different ways
# Position
# Keyword
# default
# variableLength

# **** Position ****
#Position variable means, pass the arguments in exact order defined in function
def person(name,age):
    print(name,age)

person('satish',26)

# **** Keyword ****
# when we don't know the defined order of arguments in function, we can pass the arguments values using this wau
#below we didn't passed the values as per function, but we got the correct output by define the values using argument name
person(age=26,name='Satish')

# **** default ****
# When we dont pass the value for the argument in a function, we can pass the value by default in a function
#Here we passing the group value by default, if we didn't pass the value for group then it pass default value
def college(name, group='BSC'):
    print(name,group)
college("Nalanada")

#if we pass the value then it override the default value with this passed arguments
college("Nalanda","MSCS")

# ****  variable length ****
#if we don't know how many number of arguments need to pass, then we can use this way
def sum(a,*b):
    c=a;
    for i in b:
        c=c+i
    print(c)

# * represents it can be n number of values and it will be in tuple format
