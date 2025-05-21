import random

# Generate a random array of 10 integers between 1 and 100
arr = [random.randint(1, 100) for _ in range(10)]
print("Random array:", arr)


# for i in range(1,len(arr)):
#     j=i
#     while j-1 >= 0  and arr[j] < arr[j-1]:
#         arr[j],arr[j-1] = arr[j-1],arr[j]
#         j-=1

# print(arr)


for i in range(1,len(arr)):
    j=i
    while j-1 >= 0 and arr[j-1] > arr[j]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j-=1
print(arr)