array = [43,12,67,41,52,14,5,11,8,27]

# Selection Sort
# for i in range(len(array)-1):
#     for j in range(i+1,len(array)):
#         if array[i] > array[j]:
#             array[i],array[j] = array[j],array[i]
# print(array)

# Bubble Sort
for i in range(len(array)):
    swapped= False
    for j in range(len(array)-i):
        if j+1 < len(array) and array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
            swapped = True
    if not swapped:
        break
print(array)