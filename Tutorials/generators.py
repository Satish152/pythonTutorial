# Generator is the concepts which internally used in the iterator, Generator makes the function to gives
# data in iterator format, for the generator method, we should use "yield" keyword to return the data

#When using yiled with loops, it's should be iterate through while or for loop, using next() method wont; work


def genEx(data):
    a=0
    while a<len(data):
        yield  data[a]
        a+=1

def genEx2():
    yield  1
    yield  2
    yield  3
    yield  4

list=[1,2,3,4,"satish"]
testData=genEx(list)

for i in testData:
    print(i)
#to work with next method in generator, every yield should return separately
testDt=genEx2()
print(next(testDt))
print(testDt.__next__())
print(testDt.__next__())
print(testDt.__next__())
