arr = [2,1,6,34,78,456,231,45,62]

def build_heap(arr,size):
    index = int(size)//2 - 1
    while index >=0:
        heapify(arr,index,size)
        index-=1

def heapify(arr,index,size):
    left = 2 * index + 1
    right = left + 1

    max=index

    if left < size and arr[left] > arr[index]:
        max=left
    if right < size and arr[right] > arr[max]:
        max=right

    if max!=index:
        arr[max],arr[index] = arr[index],arr[max]
        heapify(arr,max,size)

build_heap(arr,len(arr))        
print(arr)