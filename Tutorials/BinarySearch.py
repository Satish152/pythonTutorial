class binary:
    def binSearch(self,list,num):
        list.sort()
        lb=0
        ub=len(list)-1
        if lb<=ub:
            for i in range(len(list)):
                median = int((lb + ub) / 2)
                val=list[median]
                if val==num:
                    return median
                elif list[median]<num:
                    lb=median
                elif list[median]>num:
                    ub=median
            else:
                return 0

binObj=binary()
list=[15,40,97,39,68,26,32,75,79,42]

print(binObj.binSearch(list,79))