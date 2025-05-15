import random

# Generate a random array of 10 integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]
print("Random array:", arr)

result=[]

def build_heap(arr,size):
    i = int(size / 2)
    
    while i >= 0:
        heapify(i,arr,size)
        i-=1

def heapify(i,arr,size):
    left = 2 * i + 1
    right = left + 1

    max = i

    if left < size and arr[left] > arr[max]:
        max = left
    
    if right < size and arr[right] > arr[max]:
        max = right
    

    if i != max:
        arr[max],arr[i] = arr[i],arr[max]
        heapify(max,arr,size)

def heapsort(arr):
    size = len(arr)
    build_heap(arr, size)
    for i in range(size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify(0,arr,i)  

heapsort(arr)
print("Sorted array:", arr)