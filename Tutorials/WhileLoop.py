#while loop is act same as java while loop but in Python "{" is replaced with ":' and it followed the same space indent
# like if statement
a=1
while(a<5):
    print(a)
    a=a+1

a=1
b=1
while(a<5):
    print("Satish ")
    b=1
    while(b<5):
        print(b )
        b=b+1
    a=a+1

#To print content in single line
a=1
b=1
while(a<5):
    print("Satish ",end="")
    b=1
    while(b<5):
        print(b ,end=" ")
        b=b+1
    a=a+1
    print()