array = [11,23,25,26,29,33,45,59,61,63,70]

# Binary Search using DP

# def binarySearch(array,number,left,right):

#     if left > right:
#         return 0
#     mid_index = (left + right) // 2 

#     if number == array[mid_index]:
#         return 1
#     elif number > array[mid_index]:
#         return binarySearch(array,number,mid_index+1,right)
#     else:
#         return binarySearch(array,number,left,mid_index-1)

# print(binarySearch(array,26,0,len(array)-1))


# Binary Search Normal

left = 0
right=len(array)-1

number = 26

while left<=right:

    mid = (left + right + 1) // 2

    if array[mid] == number:
        print("Found")
        break
    elif number > array[mid]:
        left = mid+1
    else:
        right = mid -1
else:
    print("Not Found")