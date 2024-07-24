def binarySearch(arr,start,end,key):
    if start<=end:
        mid = (start+end)//2

        if arr[mid]==key:
            return 1
        if arr[mid] < key:
            return binarySearch(arr,mid+1,end,key)
        else:
            return binarySearch(arr,start,mid-1,key)
    else:
        return 0        



arr=[1,2,3,4,5,6,7,8,9,10]
start=0
end=len(arr)-1
key=23
print(binarySearch(arr,start,end,key))