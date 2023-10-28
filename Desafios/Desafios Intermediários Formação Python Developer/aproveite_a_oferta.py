# T = int(input()) 
# while T > 0: 
#     T -= 1 
#     N, K = input().split() 
#     N = int(N) 
#     K = int(K) 

# total = int(int(N % K) + int(N / K)) 
# print(total)


T = int(input()) 
# while T > 0: 
#     T -= 1 
#     N, K = input().split() 
#     N = int(N) 
#     K = int(K) 
#     total = int(int(N % K) + int(N / K)) 
#     print(total)

for i in range(T):
    
    N, K = input().split()
    A = int(N)
    B = int(K)
    
    if B > A:
        print(A)
    else:
        print((A % B) + (A // B))