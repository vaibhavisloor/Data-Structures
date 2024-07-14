arr = [2,5,1,78,34,56,3,9,66]
print(arr)
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)            