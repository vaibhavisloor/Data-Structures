arr = [2,1,6,34,78,456,231,45,62]

# def heap_sort(size):
#     build_heap(arr,len(arr))
#     end=len(arr)-1
#     while size > 1:
#         arr[size-1],arr[0] = arr[0],arr[size-1]
#         size-=1
#         heapify(arr,0,size)


# def build_heap(arr,size):
#     index = int(size)//2 - 1
#     while index >=0:
#         heapify(arr,index,size)
#         index-=1

# def heapify(arr,index,size):
#     left = 2 * index + 1
#     right = left + 1

#     max=index

#     if left < size and arr[left] > arr[index]:
#         max=left
#     if right < size and arr[right] > arr[max]:
#         max=right

#     if max!=index:
#         arr[max],arr[index] = arr[index],arr[max]
#         heapify(arr,max,size)

# heap_sort(len(arr))
# print(arr)

# start=0
# end = len(arr) - 1

# def quick_sort(start,end):
#     if start >= end:
#         return
    
#     pivot=end

#     left=start
#     right=end-1

#     while left<=right:
#         while left <= right and arr[left] < arr[pivot]:
#             left+=1

#         while left <= right and arr[right] > arr[pivot]:
#             right-=1

#         if left <= right :
#             arr[left],arr[right] = arr[right],arr[left]
#             left+=1
#             right-=1 
#     arr[left],arr[pivot] = arr[pivot],arr[left]
#     quick_sort(start,left-1)                
#     quick_sort(left+1,end)                


# quick_sort(start,end)
# print(arr)


# def fib(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fib(num-1) + fib(num-2)

# print(fib(7))

# def fib(index):
#     fib = [None] * (index + 1)
#     fib[0] = 0
#     fib[1] = 1

#     for i in range(2,index + 1):
#         fib[i] = fib[i-2] + fib[i-1]
#     return fib[index]   

# print(fib(5))

# N=10
# memo = [None] * (N + 1)

# def fib(index,memo):
#     if index <= 1:
#         return index
#     elif memo[index] != None:
#         return memo[index]
#     else:
#         memo[index] = fib(index-1,memo) + fib(index-2,memo)
#     return memo[index]

# print(fib(N,memo))
# print(memo)


# Merge Sort
# def merge(arr,start,mid,end):
#     temp = [None] * (end - start + 1)
#     k=0

#     i=start
#     j=mid+1

#     while i<=mid and j<=end:
#         if arr[i] < arr[j]:
#             temp[k] = arr[i]
#             i+=1
#         else:
#             temp[k] = arr[j]
#             j+=1
#         k+=1

#     while i<= mid:
#         temp[k] = arr[i]
#         i+=1
#         k+=1

#     while j<= end:
#         temp[k] = arr[j]
#         j+=1
#         k+=1

#     k=0

#     for i in range(len(temp)):
#         arr[start+i] = temp[i]

# def merge_sort(arr,start,end):
#     if start < end:
#         mid = (start + end) // 2
#         merge_sort(arr,start,mid)
#         merge_sort(arr,mid + 1,end)
#         merge(arr,start,mid,end)

# arr=[23,21,34,32,22,37,1,91,19,12,10]
# merge_sort(arr,0,len(arr)-1)
# print(arr)

# numbers = 37

# binary = ''

# while numbers >= 1:
#     rem = numbers % 2
#     numbers = numbers // 2
#     binary+=str(rem) 

# print(binary[::-1])

# from itertools import permutations
# s='abc'

# a=permutations(s)

# for perm in a:
#     print(perm)


# def bs(start,end,key):
#     while start <end:
#         mid = (start+end)//2

#         if nums[mid] == key:
#             return mid
#         else:
#             if nums[mid] > key:
#                 end=mid-1
#             else:
#                 start+=1

    
# nums = [3,89,19,13,22,56,9,93]
# nums.sort()
# print(nums)
# print(bs(0,len(nums)-1,22))

# def fib(n):
#     fib=[-1]*(n+1)
#     fib[0] = 0
#     fib[1]=1

#     for i in range(2,n+1):
#         fib[i] = fib[i-2] + fib[i-1]
#     print(fib[n-1])
# fib(5)


# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(5))


# Happy Number

seen = set()
def happy_number(n):
    global seen
    num = sum(int(i)**2 for i in str(n))
    if num == 1:
        return True
    elif num in seen:
        return False
    else:
        seen.add(num)
    return happy_number(num)
print(happy_number(13))