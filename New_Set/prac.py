arr = [7, 23, 4, 91, 16, 38, 2, 75, 44, 11]

def merge(array1, array2):
    i = 0 
    j = 0
    result = []
    print(f'This is array 1 - {array1}')
    print(f'This is array 2 - {array2}')

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1

    if j < len(array2):
        result.extend(array2[j:])

    if i < len(array1):
        result.extend(array1[i:])

    print(result)
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

merge_sort(arr)