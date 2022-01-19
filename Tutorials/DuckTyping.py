# Duck typing is a one of the type in Python polymorphism..

class A:
    def execute(self):
        print("Execute from class A")

class B:
    def execute(self):
        print("Execute from class B")

class C:
    def running(self,ide):
        ide.execute()

#here Class A and B have same function execute, so irrespective of object that we pass in running method
# execute function is Class C works successfully. this is called as duck typing
ide=A()


cls=C()
cls.running(ide)