# We are trying to implement inner Class concept usng python

class Student:

    def __init__(self,group,year):
        self.group=group
        self.year=year
        self.lap=self.Laptop("HP",20)

    def show_student_info(self):
        print(self.group,self.year)
        print(self.lap.brand,self.lap.ram)

    class Laptop:
        def __init__(self,brand,ram):
            self.brand=brand
            self.ram=ram

        def show(self):
            print(self.brand,self.ram)
cl1= Student("BSC",2)
cl1.show_student_info()
lap2=Student.Laptop("ACER",16)
lap2.show()