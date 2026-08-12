import random

array = [random.randint(0, 100) for _ in range(10)]
print("Original array:", array)

# def quick_sort(array,start,end):
#     if start >= end:
#         return

#     pivot = end
#     left = start
#     right = pivot - 1

#     while left < right:
#         while left < len(array) and array[left] <= array[pivot]:
#             left+=1

#         while right < len(array) and array[right] >= array[pivot]:
#             right-=1

#         if left < right:
#             array[left],array[right] = array[right],array[left]

#     array[pivot],array[left] = array[left],array[pivot]

#     quick_sort(array, start, left - 1)
#     quick_sort(array, left + 1, end)

# quick_sort(array,0,len(array)-1)

# print(array)


def quick_sort(arr,start,end):
    if start >= end:
        return 
    
    pivot = end
    left = start
    right = pivot - 1

    while left <= right:
        while left < len(arr) and arr[left] < arr[pivot]:
            left+=1
        
        while right >= 0 and arr[right] > arr[pivot]:
            right-=1

        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
    
    arr[pivot],arr[left] = arr[left],arr[pivot]

    quick_sort(arr,start,left-1)
    quick_sort(arr,left+1,end)

quick_sort(array,0,len(array)-1)
print(array)

    