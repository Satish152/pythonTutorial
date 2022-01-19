# output : 0 1 1 2 3 5 8 13...

def fibinoci(n):
    if n<=0 or n==1:
        print("nothing to print for 0 or less than zero or for 1 range")
    else:
        a=0
        b=1
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if(c<n):
               print(c,end=" ")

fibinoci(100)