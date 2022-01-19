# Like Class and Object in java, in python also we have a concept of class and object
# we can define a class by using 'class' keyword and same like java constructor, we need to define constructor
# with same class name

class Computer:

# init is the method which calss in background when we created a constrictor and if we want to pass a arguments
# in constructor, we can pass them directly but we need to resdefine the __init__ methof as define below

 #in every function, self is a default and it takes object we created using constrcctor as invoker
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu

    def config(self):   #when we want to use the constrcutor arguments, we can call them directly using below syntax
        print("ACER,",self.ram,",",self.cpu)


    def compare(self, other):
        if self.ram == other.ram:
            print("they are equal")
        else:
            print("they are not equal")

com1=Computer(16,"i5")
com2=Computer(12,"i5")

com1.config()


#comparing 2 objects
com1.compare(com2);

