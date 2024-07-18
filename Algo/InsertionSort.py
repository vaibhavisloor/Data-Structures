arr = [2,1,6,34,78,456,231,45,62]
print(arr)

for i in range(1,len(arr)):
    value = arr[i]
    index = i

    while index > 0 and arr[index-1] > value:
        arr[index] = arr[index-1]
        index-=1
    arr[index] = value

print(arr)
