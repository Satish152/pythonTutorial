
for i in range(1,25):
    if(i%2==0):
        continue
    else:
        print(i)

list=[1,5,3,7,6,4,'*',9,2,3]
for i in list:
    if(i=='*'):
        break
    else:
        print(i)

#pass is just skip that block and continue with further lines of code in the statement but "continue" just kip the
#current iteration and go with next iteration

for i in list:
    if(i=='*'):
        pass
    else:
        print(i)
    print("bye")

