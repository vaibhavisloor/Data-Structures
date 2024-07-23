def BuildHeap(arr,size):
    i=int(size/2)
    while i>=0:
        Heapify(arr,i,size)
        i-=1

def Heapify(arr,index,size):

    left = 2 * index + 1
    right = left + 1

    max_ = index

    if left <= size and arr[left] > arr[max_]:
        max_=left 

    if right <= size and arr[right] > arr[max_]:
        max_ = right

    if index != max_:
        arr[index],arr[max_]=arr[max_],arr[index]
        Heapify(arr,max_,size)            



if __name__ == "__main__":
    arr = [10, 20, 40, 30, 80, 60, 50]

    print(arr)
    BuildHeap(arr,len(arr)-1)
    print(arr)
