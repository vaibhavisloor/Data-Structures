import random

# Generate a random array of 10 integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]
print("Random array:", arr)



for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)