
# # def merge(array1, array2):
# #     i = 0 
# #     j = 0
# #     result = []
# #     print(f'This is array 1 - {array1}')
# #     print(f'This is array 2 - {array2}')

# #     while i < len(array1) and j < len(array2):
# #         if array1[i] < array2[j]:
# #             result.append(array1[i])
# #             i+=1
# #         else:
# #             result.append(array2[j])
# #             j+=1

# #     if j < len(array2):
# #         result.extend(array2[j:])

# #     if i < len(array1):
# #         result.extend(array1[i:])

# #     print(result)
# #     return result

# # def merge_sort(arr):
# #     if len(arr)<=1:
# #         return arr
# #     mid = len(arr) // 2
# #     left = merge_sort(arr[:mid])
# #     right = merge_sort(arr[mid:])
# #     return merge(left,right)

# # merge_sort(arr)
# arr = [7, 23, 4, 91, 16, 38, 2, 75, 44, 11]
# print(arr)
# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr

#     pivot_index = len(arr)-1
#     pivot = arr[pivot_index]
#     left = 0
#     right = len(arr)-2
#     print(pivot)
#     while left < right:
#         while arr[left] < pivot:
#             left+=1
#         while arr[right] > pivot:
#             right-=1

#         if left < right:
#             arr[left],arr[right] = arr[right],arr[left]
#             left+=1
#             right-=1

#     arr[left],arr[pivot_index] = arr[pivot_index],arr[left]
#     # print(arr)
#     return quick_sort(arr[:left]) + [pivot] + quick_sort(arr[left+1:])
# arr = quick_sort(arr)

# print(arr)


# values = [8,19,7,15,7,13,12,14,13]

# # 2 cores 
# new_list = values[:]
# while True:
#     if len(new_list) == 1:
#         print(new_list)
#         break
#     core_divisor = 2
#     result = []
#     for i in range(len(new_list)):
#         if i%core_divisor == 0:
#             if i+1 < len(new_list):
#                 new_list[i] += new_list[i+1]
#             result.append(new_list[i])
#         else:
#             pass
#     new_list=result
#     print(result)

#2^n cores
# values = [8,19,7,15,7,13,12,14]
# new_list = values[:]
# while True:
#     if len(new_list) == 1:
#         print(new_list)
#         break
#     core_divisor = 3
#     result = []
#     for i in range(len(new_list)):
#         if i%core_divisor == 0:
#             j=i+1
#             while j%core_divisor!=0 and j < len(new_list):
#                 new_list[i] += new_list[j]
#                 j+=1
#                 # print(j)
#             result.append(new_list[i])
#         else:
#             pass
#     new_list=result 
#     print(result)

print(int(None))