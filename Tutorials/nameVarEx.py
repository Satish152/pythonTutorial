
def test():
    print(__name__) # it returns output as __main__
    print("this is main class")

# if we print this name variable it gives the output as main which means script executing in same class

# here we placing condition like __name__ returning output as __main__ then execute the test() method
if __name__=="__main__":
    test()