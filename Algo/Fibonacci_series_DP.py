# Top down without Memoization

# def fib(num):
#     if num == 0:
#         return 0
#     if num==1:
#         return 1
#     else:
#         return fib(num-1) + fib(num-2)

# print(fib(2))    
    
# Bottom Up 

# N=10

# fib=[None] * (N+1)

# fib[0]=0
# fib[1]=1

# for i in range(2,N+1):
#     fib[i]=fib[i-1]+fib[i-2]

# print(fib[N-1])


# Top down approach with memoization
# Memoization is a technique used in top down approach of dynamic programming, where there is no need to recompute redundantly 

N=10

memo=[None]* (N+1)

def fibonacci(N,memo):
    if N<=1:
        return N
    elif memo[N] is not None:
        return memo[N]     
    else:
        memo[N] = fibonacci(N-1,memo) + fibonacci(N-2,memo)
    return memo[N]    
    
print(fibonacci(N,memo))    

