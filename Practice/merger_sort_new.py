a = [42, 7, 91, 18, 63, 5, 77, 34, 12, 56, 89, 23, 68, 3, 45, 81, 29, 14, 97, 51]

def merge(array1, array2):
    i=0
    j=0 
    result = []

    while i<len(array1) and j<len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1
    if j<len(array2):
        result.extend(array2[j:])
    if i<len(array1):
        result.extend(array1[i:])

    return result

def merge_sort(array):
    if len(array) <=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left,right)


# print(f"This is MERGE SORT \n{merge_sort(a)}")




def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = len(array)-1

    left = 0
    right = pivot-1

    while left < right:
        while left<=right and array[left] <= array[pivot]:
            left+=1
        while left<=right and array[right] > array[pivot]:
            right-=1

        if left < right:
            array[left],array[right] = array[right],array[left]
    array[left],array[pivot] = array[pivot],array[left]


    return quick_sort(array[:left]) + [array[left]] + quick_sort(array[left+1:])


print(f"This is QUICKSORT \n{quick_sort(a)}")