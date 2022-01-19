# overloading in python is not like a java.. like java, it won't consider the method signatures to overload
# a method, instead of that we can overload a method in another way

class A:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

clsA=A()
clsA.sum(2,5,6)

# here we overriding the sum method from class A to class B with same nethod name
class B(A):
    def sum(self,a,b):
        print(a+b)

clsB=B()
clsB.sum(1,5)