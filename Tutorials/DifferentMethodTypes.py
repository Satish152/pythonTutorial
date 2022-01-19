# In python, we can create functions by passing a default variable self which is complete based on object behaviour
# in the same way we can pass another argument type called 'cls' which is used to deal with class level vars
# but when we use the 'cls' arguments, we eneed to use decorator classed "@classMethod" to let python know that it
# is class level method and we have another method which don't required either class or self argumentd, which we
# we can call it as static methods

class Test:
    school="Navodaya"
    status=""
    total=0

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def sum(self):
        global  total
        total=self.m1+self.m2+self.m3
        print(total)

    @classmethod
    def student_status(cls):
        print(total)
        if(total>=36):
            print("student pass", cls.school)
        else:
            print("student fail")

    def getSchoolName(self):
        print("this is a test method")

s1=Test(36,45,98)
s1.sum()
Test.student_status()



