array = [2,1,4,3,21,4,78,9,7,13,45]

def build_heap(array, size):
    i= int (size//2)
    while i >=0:
        Heapify(array,i,size)
        i-=1

def Heapify(array,i,size):

    left = 2*i + 1
    right = 2*i + 2

    max = i

    if left<=size and array[left] > array[max]:
        max = left
    
    if right<=size and array[right] > array[max]:
        max = right

    if max!=i:
        array[max],array[i] = array[i],array[max]
        Heapify(array,max,size)
    
build_heap(array,len(array)-1)
print(array)

    




    