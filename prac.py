arr = [2,1,6,34,78,456,231,45,62]

# def heap_sort(size):
#     build_heap(arr,len(arr))
#     end=len(arr)-1
#     while size > 1:
#         arr[size-1],arr[0] = arr[0],arr[size-1]
#         size-=1
#         heapify(arr,0,size)


# def build_heap(arr,size):
#     index = int(size)//2 - 1
#     while index >=0:
#         heapify(arr,index,size)
#         index-=1

# def heapify(arr,index,size):
#     left = 2 * index + 1
#     right = left + 1

#     max=index

#     if left < size and arr[left] > arr[index]:
#         max=left
#     if right < size and arr[right] > arr[max]:
#         max=right

#     if max!=index:
#         arr[max],arr[index] = arr[index],arr[max]
#         heapify(arr,max,size)

# heap_sort(len(arr))
# print(arr)

start=0
end = len(arr) - 1

def quick_sort(start,end):
    if start >= end:
        return
    
    pivot=end

    left=start
    right=end-1

    while left<=right:
        while left <= right and arr[left] < arr[pivot]:
            left+=1

        while left <= right and arr[right] > arr[pivot]:
            right-=1

        if left <= right :
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1 
    arr[left],arr[pivot] = arr[pivot],arr[left]
    quick_sort(start,left-1)                
    quick_sort(left+1,end)                


quick_sort(start,end)
print(arr)