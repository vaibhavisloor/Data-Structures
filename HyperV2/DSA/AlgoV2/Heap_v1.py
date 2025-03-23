array = [2,1,4,3,21,4,78,9,7,13,45]

def build_heap(array, size):
    i= int (size//2)
    while i >=0:
        Heapify(array,i,size)
        i-=1

def Heapify(array,i,size):

    left = 2*i + 1
    right = 2*i + 2

    




    