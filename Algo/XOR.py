arr=[1,2,3,4,5,4,3,2,1,6]
# xor_result=0

# for num in arr:
#     xor_result ^=num

# print(xor_result)


# Two unique numbers

xor_all=0

for num in arr:
    xor_all^=num

right_set_bit = xor_all & -xor_all

num1=0
num2=0
for num in arr:
    if num & right_set_bit:
        num1^=num
    else:
        num2^=num    
print(num1,num2)        
        