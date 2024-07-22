def quick_sort(arr):
    if len(arr) <=1:
        return arr

    pivot = arr[0]

    smaller_array = [x for x in arr[1:] if x<= pivot] 
    larger_array = [x for x in arr[1:] if x > pivot] 

    less_than_pivot = quick_sort(smaller_array)
    more_than_pivot = quick_sort(larger_array)

    return less_than_pivot + [pivot] + more_than_pivot


array=[3,87,7,9,45,23,12,43,21]
print(quick_sort(array))