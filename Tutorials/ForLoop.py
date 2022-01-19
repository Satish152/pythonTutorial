#as like java, for loop won't same like python, here we can use range function to iterate for loop

list=[1,2,3,4,5]
#We can do enhanced for loop in this format
for i in list:
    print(i)

#normal iteration way for loop to iterate nums
for i in range(0,len(list)):
    print(i)

#iterating with increase wth 2 in every iteration
for i in range(5,10,2):  #it starts the iteration from 5 and iterate till 10 by adding 2
    print(i)

#you can directly define the range with out mentioned he starting and ending point
for i in range(10):
    print(i)  #it print number from 1 to 10