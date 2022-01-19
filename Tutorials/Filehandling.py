# File handling in python is very easy to use, we have a function called Open which accepts file name and
# file action attributes which r- reading, w- writing, a- append, wb- writing binary, rb- reading binary

f=open("../File/newFile",'r')

# to read total content in a file, we use read() function
#print(f.read())

# to read each line in a file, we use readLine(), it works same as next() function in iterator
#print(f.readline())
#print(f.readline()) #these 2 steps prints 2 lines in a file
#print(f.readline(4)) # in the current read till 4 characters

# readLines returns the list of lines which we can iterte through for loop
#lines=f.readlines()
#for line in lines:
#    print(line)

# write file or create a new file, we need to use file action char as W
#wf=open("../File/newFile2",'w')
# #it will check for a file with file name given, if it's not found, it creates new file
#wf.write("writing new line 1\n")
#wf.write("writing new line 2")

#when we try to write a new content in continution of exisiting file content, we habe to use action 'a'
#af=open("../File/newFile2",'a')
#af.write("\nwriting line no 3")

#now to read a binary of the image, we should use rb
iR=open("../File/myImage.jpg",'rb')

#copy of the image using 'wb' action
iW=open("../File/myImage2.JPG",'wb')
for line in iR:
    iW.write(line)


