# arr = [2,1,6,34,78,456,231,45,62]

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

# seen = set()
# def happy_number(n):
#     global seen
#     num = sum(int(i)**2 for i in str(n))
#     if num == 1:
#         return True
#     elif num in seen:
#         return False
#     else:
#         seen.add(num)
#     return happy_number(num)
# print(happy_number(13))


# Max Heap

# def build_heap(arr,size):
#     index=size//2 - 1
#     while index >=0:
#         heapify(arr,index,size)
#         index-=1
# def heapify(arr,index,size):
#     left =  2 * index + 1
#     right = left + 1

#     max = index

#     if left < size and arr[left] > arr[max]:
#         max = left
#     if right < size and arr[right] > arr[max]:
#         max = right
    
#     if max != index:
#         arr[ max], arr[index] = arr[ index], arr[max]
#         heapify(arr, max,size)
# arr = [10, 20, 40, 30, 80, 60, 50]
# print( arr)
# build_heap(arr, len(arr))
# print( arr)


# N=10
# memo=[None]*(N+1)

# def fib(n,memo):
#     if n<=1:
#         return 1

#     if memo[n] is not None:
#         return memo[n]
#     else:
#         memo[n] = fib(n-1,memo) + fib(n-2,memo)
#     return memo[n]
    
# print(fib(5,memo))




# sample_array = [5, 12, 7, 3, 9, 15, 8, 21, 4, 10]
# print(sample_array)
# n=len(sample_array)

# Selection Sort
# for i in range(n):
#     for j in range(i+1,n):
#         if sample_array[i] > sample_array[j]:
#             sample_array[i],sample_array[j] = sample_array[j],sample_array[i]
# print(sample_array)


# Bubble Sort

# for i in range(n-1):
#     swap = False
#     for j in range(n-1-i):
#         if sample_array[j] > sample_array[j+1] :
#             sample_array[j],sample_array[j+1] = sample_array[j+1],sample_array[j]
#             swap = True
    
#     if swap == False:
#         break
# print(sample_array)



# Max Heap

# def build_heap(arr):
#     index = len(arr) // 2 - 1
#     while index >= 0:
#         heapify(arr,index,len(arr))
#         index -= 1

# def heapify(arr,index,size):
#     left = 2 * index + 1
#     right = left + 1

#     max = index

#     if left < size and arr[left] > arr[max]:
#         max = left
#     if right < size and arr[right] > arr[max]:
#         max = right

#     if index != max:
#         arr[max],arr[index] = arr[index],arr[max]
#         heapify(arr,max,size)

# build_heap(sample_array)
# print(sample_array)


# Min Heap

# def build_heap(arr):
#     index = len(arr) // 2 - 1
#     while index >= 0:
#         heapify(arr,index,len(arr))
#         index -= 1

# def heapify(arr,index,size):
#     left = 2 * index + 1
#     right = left + 1

#     max = index

#     if left < size and arr[left] < arr[max]:
#         max = left
#     if right < size and arr[right] < arr[max]:
#         max = right

#     if index != max:
#         arr[max],arr[index] = arr[index],arr[max]
#         heapify(arr,max,size)

# build_heap(sample_array)
# print(sample_array)

# Heap Sort

# Max Heap
# final_array=[]
# def build_heap(arr,size):
#     index = len(arr) // 2 - 1
#     while index >= 0:
#         heapify(arr,index,size)
#         index -= 1

# def heapify(arr,index,size):
#     left = 2 * index + 1
#     right = left + 1

#     max = index

#     if left < size and arr[left] > arr[max]:
#         max = left
#     if right < size and arr[right] > arr[max]:
#         max = right

#     if index != max:
#         arr[max],arr[index] = arr[index],arr[max]
#         heapify(arr,max,size)
# def heap_sort(arr,size):
#     build_heap(arr,size)

#     while size > 0:
#         arr[0],arr[size] = arr[size],arr[0]
#         size-=1
#         heapify(arr,0,size)


# heap_sort(sample_array,len(sample_array)-1)
# print(sample_array)

# def quick_sort(arr,start,end):
#     if start >= end:
#         return
    
#     left = start
#     pivot = end
#     right = end - 1

#     while True:
#         while left <= right and arr[left] < arr[pivot]:
#             left +=1
#         while left <= right and arr[right] > arr[pivot]:
#             right-=1

#         if left < right:
#             arr[left],arr[right] = arr[right],arr[left]
#         else:
#             break
#     arr[left], arr[pivot] = arr[pivot], arr[left]

#     quick_sort(arr,start,left-1)
#     quick_sort(arr,left+1,end)

# quick_sort(sample_array,0,len(sample_array)-1)
# print(sample_array)


# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def add_first(self,val):
#         if self.head is None:
#             self.head = Node(val)
#         else:
#             newNode = Node(val)
#             newNode.next = self.head
#             self.head = newNode
    
#     def add_last(self,val):
#         if self.head is None:
#             self.head = Node(val)
#         else:
#             temp = self.head
#             while temp.next != None:
#                 temp =temp.next

#             temp.next = Node(val)
    
#     def delete(self,val):
#         if not self.head:
#             return "Empty List"
#         elif self.head.val == val:
#             self.head = self.head.next
#             return f"{val} has been deleted"
#         else:
#             temp = self.head
#             while temp.next != None:
#                 if temp.next.val == val:
#                     temp.next = temp.next.next
#                     return f"{val} has been deleted"
#                 temp=temp.next
#             return "Value not found"

#     def search(self,val):
#         if not self.head:
#             return "Empty List"
#         else:
#             temp = self.head
#             while temp != None:
#                 if temp.val == val:
#                     return(f"Found {val}")
#                 temp = temp.next
#             return("Not Found")
        
#     def print(self):
#         if self.head is None:
#             return "Empty List"
#         else:
#             temp=self.head
#             while temp != None:
#                 print(temp.val, end=" ")
#                 temp = temp.next
            
# LL = LinkedList()

# LL.add_first(10)
# LL.add_first(20)
# LL.add_first(30)
# LL.add_first(40)
# LL.add_first(50)
# LL.add_first(60)
# LL.add_last(100)
# LL.delete(10)
# LL.print()
# print(LL.search(40))



# class Queue:
#     def __init__(self,size):
#         self.size = size
#         self.front=-1
#         self.rear=-1
#         self.array=[None] * size

#     def add_to_queue(self,val):
#         if self.rear == -1:
#             self.rear=0
#             self.front=0

#             self.array[self.rear] = val

#         elif self.rear + 1 < self.size:
#             self.rear+=1
#             self.array[self.rear] = val
#         else:
#             print("Queue is full")
    
#     def remove_element(self):
#         if self.front == -1:
#             print("Queue is empty")
#         elif self.front < self.rear:
#             print(f"{self.array[self.front]} is removed.")
#             self.array[self.front] = None
#             self.front+=1
#         elif self.front==self.rear:
#             print(f"{self.array[self.front]} is removed.")
#             print("Queue is empty")
#             self.front = -1
#             self.rear = -1
            

#     def print_queue(self):
#         return(self.array[self.front:self.rear+1])

# q=Queue(5)

# q.add_to_queue(10)
# q.add_to_queue(20)
# q.add_to_queue(30)
# q.add_to_queue(40)
# q.add_to_queue(50)
# q.add_to_queue(60)
# q.add_to_queue(70)
# print(q.print_queue())
# q.remove_element()
# print(q.print_queue())
# q.remove_element()
# print(q.print_queue())
# # q.add_to_queue(10)



class Queue:
    def __init__(self,size):
        self.size = size
        self.array = [None] * size
        self.front = -1
        self.rear = -1