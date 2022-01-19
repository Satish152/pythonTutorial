
num=16

for i in range(2,num):
    if num % i==0:
        print(num,' not a prime')
        break
else:
    print(num,' is a prime number')

#prime number from 2 - 100
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")