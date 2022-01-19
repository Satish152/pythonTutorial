class LineasrSearch:
    def search(self,list,num):
        length=len(list)
        for i in range(length):
            if list[i]==num:
                return i
        else:
            return 0
list=[2,6,7,9,8,7,3,6]
linearObj=LineasrSearch()
result=linearObj.search(list,9)
if result==0:
    print("Not found")
else:
    print("Found the value at index ",result)