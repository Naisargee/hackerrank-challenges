def isprime(n):
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5;w = 2
    while i * i <= n:
        if n % i == 0: return False
        i += w;w = 6 - w
    return True


T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    if m==1: print(2)
    elif isprime(m):
        if n%2==0: print(2)
        else: print(1)
    else:
        if n%2!=0: print(1)
        else: print(2)
