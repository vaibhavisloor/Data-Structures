def binarySearch(arr,key):
    start=0
    end = len(arr)-1


    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return 1
        if arr[mid] < key:
            start=mid+1
        else:
            end=mid-1    

if __name__ == "__main__":
    nums = [3,9,13,19,22,56,89,93] #Array has to be sorted for BS

    print(binarySearch(nums,22))
