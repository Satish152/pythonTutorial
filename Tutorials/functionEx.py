def add(x,y):
    z=x+y
    print(z)

add(5,6)

def sum(x,y):
    return x+y

print(sum(4,6))

#return two outputs in tuple
def sum_sub(x,y):
    a=x+y
    b=x-y
    return a,b

print(sum_sub(9,9))

#we can assign it multiple return output to multiple variables
result,result1=sum_sub(9,9)

print(result)
print(result1)
