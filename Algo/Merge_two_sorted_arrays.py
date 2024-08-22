arr1 = [21,12,27,54,3,2,62,9,15,3,97]
arr2 = [31,82,11,21,29,36,62,41,19,34]
arr1.sort()
arr2.sort()
print(arr1,arr2)
arr3=[]
i=0
j=0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i+=1
    elif arr1[i] > arr2[j]:
        arr3.append(arr2[j])
        j+=1   
    else:
        arr3.append(arr1[i])    
        arr3.append(arr2[j])
        i+=1
        j+=1
if i >= len(arr1) and j < len(arr2):
    arr3.extend(arr2[j:])

if j >= len(arr2) and i < len(arr1):
    arr3.extend(arr1[i:])

print(arr3)    


