a=[1,3,5,7,9]
b=[2,4,6,8,10]
i_a=0
i_b=0

sorted_array=[]

while i_a <= len(a)-1:
    if a[i_a] < b[i_b]:
        sorted_array.append(a[i_a])
        i_a+=1
    elif a[i_a] > b[i_b]:
        sorted_array.append(b[i_b])
        i_b+=1
    else:
        sorted_array.append([a[i_a],a[i_a]])
        i_a+=1
        i_b+=1
    print(sorted_array)    
    
for num in b[i_b:]:
    sorted_array.append(num)
print(sorted_array)     