def sel_sort(data):

    for i in range(1,len(data)):
        minpos=i
        for j in range(i,len(data)):
            if data[minpos]>data[j]:
                minpos=j
        temp=data[i]
        data[i]=data[minpos]
        data[minpos]=temp
        print(data)


arr=[2,5,7,9,6,3,4]
sel_sort(arr)