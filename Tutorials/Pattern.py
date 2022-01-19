#printing patterns

#* * * *
#* * * *
#* * * *
#* * * *

for i in range(4):
    for j in range(4):
        print(" * ",end="")
    print()

print()
# *
# * *
# * * *
# * * * *

for i in range(4):
    for j in range(i+1):
        print(" * ",end="")
    print()
print()

# * * * *
# * * *
# * *
# *

for i in range(4):
    for j in range(4-i):
        print(" * ",end="")
    print()
print()

exec=False
for i in range(4):
    exec = False
    for j in range(4):
        if i!=0 and exec==False:
            for k in range(i):
                print(" ",end="")
                exec=True
        else:
            print(" * ",end="")
    print()
