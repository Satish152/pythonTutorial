#Tuple is same like a list which defined by using "()" but it doesn't have any previlige to do action on items
#means we can't edit,add,remove and delete the items.. because of this, execution process is speed up compared to list

#Set is defined as {} and it doesn't allow duplicates and calling element with index is not allowed

tups=(1,5,7,"Satish")

print(tups)
print(tups[3])

sets={1,2,1,4,5,3}
print(sets)

for i in range(5,10,2):
    sets.add(i)

print(sets)
