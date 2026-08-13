def BuildHeap(arr, size):

    i = int(size / 2)
    
    while i >= 0:
        Heapify(arr,i,size)
        i -= 1   

def Heapify(arr, index, size):

    left = 2 * index + 1
    right = left + 1

    max = index

    if left < size and arr[left] > arr[max]:
        max = left

    if right < size and arr[right] > arr[max]:
        max = right

    if index != max:
        arr[max],arr[index] = arr[index],arr[max]
        Heapify(arr,max,size)

if __name__ == '__main__':
	
	arr = [10, 20, 40, 30, 80, 60, 50]

	print("The Array Elements Are:")
	for i in arr:
		print(i, end=" ")

	print("\nConstructing Heap...")
	BuildHeap(arr, len(arr)-1)
	
	print("The Array Elements Are:")
	for i in range(len(arr)):
		print(arr[i], end=" ")