import random

# Generate a random array of 10 integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]
print("Random array:", arr)


# for i in range(len(arr)-1):
#     swapped = False
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             swapped = True
#     if not swapped:
#         break

# print(arr)
    
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)