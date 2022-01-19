# iterator is the option helps to iterte the objects which are enabled for iteration
# we can use iter function to pass the iterable data and need to assign that iter to a object
# we can use either iterObj.__next__() function or passing iterobj as a argument in next() function

class Test:

    list=["A","B","C",1,2,3]

    it=iter(list)
    print(it.__next__())
    print(next(it))