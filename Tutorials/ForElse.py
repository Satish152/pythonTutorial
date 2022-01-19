#for else is used to get to know how exactly for loop iteration executing and what happening inside of our code block

#here in this loop we trying to find any number which is divible by 9 and if we didn't have any then our break
#wont execute at that time it reach the else block and do the mentioned action in ele block
a=[1,2,3,6,4,5,8,4,7]
for i in a:
    if i/9==0:
        break
else:
    print('not found')