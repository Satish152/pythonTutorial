#  A decorator in Python is a function that takes another function as its argument, and returns yet a
#  nother function . Decorators can be extremely useful as they allow the extension of an existing function,
#  without any modification to the original function source code.

#Example 1:
def div(a,b):
    return a/b

#here we want to swap the variables if a<b, but that logic is not available in div and we didn't have access
# to modify the div function, then we use this decorator

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return  inner

#now we need to link the div function to smart div function, for that we just use the below syntax
# any object name we can use
div1=smart_div(div)
print(div1(2,4))


#Example 2:
def shout_wish(text):
    return text.upper()

def normal_wish(text):
    return text.lower()

def dec_ex(func):
    greeting=func("Hi, Welcome to Python course")
    print(greeting)

dec_ex(shout_wish)




