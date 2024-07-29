def quickSort(arr,start,end):
    if start >= end:
        return
    
    pivot=end
    left=start
    right=end-1

    while True:
        while left <= right and arr[left] <= arr[pivot]:
            left+=1
        while left <= right and arr[right] >= arr[pivot]:
            right-=1

        if left < right:
            arr[left],arr[right] = arr[right],arr[left] 
        else:
            break

    arr[left],arr[pivot] = arr[pivot],arr[left]

    quickSort(arr,start,left-1)
    quickSort(arr,left+1,end)

random_arr = [9, 32, 86, 43, 50, 40, 39, 79, 22, 65, 21, 10, 28, 19, 52]

# Sort the array using quicksort
quickSort(random_arr, 0, len(random_arr) - 1)

print(random_arr)
