import random

array = [random.randint(0, 100) for _ in range(10)]
print("Original array:", array)

def merge_sort(array,start,end):
    if start < end:
        mid = (start + end)//2
        merge_sort(array,start,mid)
        merge_sort(array,mid+1,end)
        merge(array,start,mid,end)


def merge(array,start,mid,end):
    temp = [None]*(end-start+1) 
    i = start
    j= mid + 1
    k=0

    while i <= mid and j<=end:
        if array[i] < array[j]:
            temp[k] = array[i]
            k+=1
            i+=1
        else:
            temp[k] = array[j]
            k+=1
            j+=1

    while i<=mid:
        temp[k] = array[i]
        k+=1
        i+=1
    
    while j<=end:
        temp[k] = array[j]
        k+=1
        j+=1

    for i in range(len(temp)):
        array[start+i] = temp[i]

merge_sort(array, 0, len(array) - 1)

print("Sorted array:", array)

