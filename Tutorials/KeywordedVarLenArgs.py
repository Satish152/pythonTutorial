#when we don't know no of arguments to pass in the function, we design a function with VariableLenggth arguments
#which represents as a * in function argument and return tuple from the passed data but when we want to pass the
#data based on the keywords using this functionality, we can do it as "**", which allowes the user to declare argument
#with keyword and value

# * returns tuple and ** returns dictionary
def person(name,**keyArgs):
    print(name)
    for i,j in keyArgs.items():
        print(i,j)
    print(keyArgs.get("age")) # we cand directly get key value using get function

person("Satish",age=26,city="Hyderabdd",mobile=123456)