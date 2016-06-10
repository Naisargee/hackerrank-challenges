N,M=map(int,input().strip().split())

arr=[0]*(N+1)
for _ in range(M):
    a,b,v=map(int,input().strip().split())
    arr[a]+=v
    if (b+1)<=N: arr[b+1]-=v

maxi=0
temp=0
for i in arr:
    temp=temp+i; maxi=max(temp,maxi)
print(maxi)
