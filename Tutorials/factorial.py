## 4 factorial  is 24 and % factorial is 120.. means 1*2*3*4*5

def factorial(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

print(factorial(6))

