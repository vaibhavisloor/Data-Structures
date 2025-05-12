array = [23,11,43,29,13,4,56,79,25,7]

def build_heap(array,size):
    i = len(array) // 2
    while i>=0:
        heapify(array,size,i)
        i-=1

def heapify(array,size,i):

    left = 2*i+1
    right = left + 1

    max = i

    if left <= size and array[left] > array[max]:
        max = left
    
    if right <=size and array[right] > array[max]:
        max = right

    if max!=i:
        array[max],array[i] = array[i],array[max]
        heapify(array,size,max)

build_heap(array,len(array)-1)
print(array)