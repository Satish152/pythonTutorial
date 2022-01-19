# Thread is a process which execute the tasks we are running.. we can extend the class to Thread using
# Inheritance concept and same like Java Thread contains run method and execution of thread done by start method
# we need to import Thread from the Threading module

from  threading import  *
from time import  sleep
class Test(Thread):
    def run(self) :
        for i in range(0,30):
            print("Execution from class 1")
            sleep(1)

class Tes1(Thread):
    def run(self) :
        for i in range(0, 30):
            print("Execution from class 2")
            sleep(1)

t1=Test()
t2=Tes1()

# When we call the start() function, it creates a sub thread from main thread and execute the  task
# so here it divides the main thread in to 2 threads and execute the  tasks created
t1.start()
sleep(0.2) # here we waiting for 0.2 seconds. so that two threads execute in a order
t2.start()

t1.join()
t2.join()
# this join methods tells the execution of main thread yo wait until these two threads join in to main
# This bye will be printed after execution of t1 and t2 threads
# When we want to print bye or do some action without using join function, it will start execution immediately
# after starting Thread execution
print("byee")