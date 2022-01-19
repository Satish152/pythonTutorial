
def sort(data):
    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if data[i]>data[j]:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    print(data)

def sort_2(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[i]<data[j]:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    print(data)

def descend_sort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[i]>data[j]:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    print(data)


arr=[2,5,7,9,6,3,4]
sort(arr)
sort_2(arr)
descend_sort(arr)