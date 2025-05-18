array = [20,12,2,45,21,13,17,19]
size = len(array)


def build_heap(array,size):
    i = int(size/2)
    while i >= 0:
        heapify(i,array,size)
        i-=1

def heapify(i,array,size):
    left = 2*i+1
    right = left + 1

    max = i

    if left < size and array[left] > array[max]:
        max = left
    
    if right < size and array[right] > array[max]:
        max = right
    
    if max != i:
        array[i],array[max] = array[max],array[i]
        heapify(max,array,size)

build_heap(array,size)

print(array)