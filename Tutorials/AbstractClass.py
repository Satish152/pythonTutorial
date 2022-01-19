# Python doesn't have inbuilt abstract method supoort, to make the class to support Abstract we need to import
# ABC and AbstractMethods from abc module
# In python also, it won't allows to create a object for the abstract class

from abc import ABC,abstractmethod

#to define a method as abstract we need to add decorator called abstractmethod and we need to inherit the
# ABC in to the class like  below
class desktop(ABC):

    @abstractmethod
    def wifi(self):
        pass

    def games(self):
        print("gaming supported")

class Laptop(desktop):

    def wifi(self):
        print("wifi implemented in laptop")

lap=Laptop()
lap.wifi()
lap.games()