def BuildHeap(arr,size):
    i=len(arr)//2
    while i>=0:
        Heapify(arr,i,size)
        i-=1

def Heapify(arr,index,size):
    left = 2*index + 1
    right = left+1

    max=index

    if left < size and arr[left] > arr[max]:
        max=left
    if right < size and arr[right] > arr[max]:
        max=right

    if index != max:
        arr[index],arr[max]=arr[max],arr[index]
        Heapify(arr,max,size)   

def HeapSort(arr,size):

    BuildHeap(arr,size)

    size=len(arr)-1

    while size>0:
        arr[0],arr[size]=arr[size],arr[0]
        size-=1
        Heapify(arr,0,size)

arr=[23,13,21,32,34,52,12,33]

HeapSort(arr,len(arr))
print(arr)