# Same like Java, In python also we can implement Inheritance, but In Python we can also got the ability
# to apply multiple Inheritance, that means we can inherit the multiple classes to single class at a time

class A:
    def feature1(self):
        print("I'm from Class A")

#Signle Inheritance ex
class B(A):
    def feature2(self):
        print("This is class B")
clsB=B()
# we can able to access the method present in the class A using class B objecy
clsB.feature1()
clsB.feature2()

#multi level Inheritance
class C(B):
    def feature3(self):
        print("This is from Class C")

clsC=C()
# here we inherit the Class B to C, and class B is already inherited from class A
clsC.feature1()
clsC.feature2()
clsC.feature3()

#Multiple Inheritance
class D:
    def feature4(self):
        print("This is Class D")

clsD=D()
# by using class D, we can access the methods from Class C
# this multiple inheritance concept not supported in Java

class E(A,D):
    def feature5(self):
        print("This is using multiple inheritance")

clsE=E()
clsE.feature1() #from class A
clsE.feature4() #from class D
clsE.feature5() #from class E
