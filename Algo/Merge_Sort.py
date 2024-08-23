# a=[1,3,5,7,9]
# b=[2,4,6,8,10]
# i_a=0
# i_b=0

# sorted_array=[]

# while i_a <= len(a)-1:
#     if a[i_a] < b[i_b]:
#         sorted_array.append(a[i_a])
#         i_a+=1
#     elif a[i_a] > b[i_b]:
#         sorted_array.append(b[i_b])
#         i_b+=1
#     else:
#         sorted_array.append([a[i_a],a[i_a]])
#         i_a+=1
#         i_b+=1
#     print(sorted_array)    
    
# for num in b[i_b:]:
#     sorted_array.append(num)
# print(sorted_array)     


def merge(arr,start,mid,end):
    temp = [None] * (end-start+1)

    i=0
    j = mid + 1
    k=0

    while i<=mid and j<=end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1
    while i<=mid:
        temp[k] = temp[i]
        i+=1
    while j<=mid:
        temp[k] = temp[j]
        j+=1 

    k=0

    for i in range(end-start+1):
        arr[i] = arr[k]
        k+=1       



def merge_sort(arr,start,end):
    if start < end:
        mid = (start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,start,mid,end)