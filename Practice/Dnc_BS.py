array = [1,3,4,6,7,8,10,13,15,16,20]

def binarySearch(start,end,key):
    mid = (start + end) // 2

    if start > end:
        return False

    if array[mid] == key:
        return True
    else:
        if array[mid] < key:
            return binarySearch(mid+1,end,key)
        elif array[mid] > key:
            return binarySearch(start,mid-1,key)
        

print(binarySearch(0,len(array)-1,14))


