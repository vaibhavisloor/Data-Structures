def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n=sum(int(digit)**2 for digit in str(n))
    return n==1    

number = 23
if is_happy(number):
    print("Happy Number")
else:
    print("Not a Happy Number")    