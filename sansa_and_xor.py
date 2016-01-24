T=int(input())
for _ in range(0,T):
    N=int(input())
    nums=list(map(int,input().split()))
    if N%2==0:
        print(0)
        continue
    ans=0
    i=0
    while i<len(nums):
        ans=ans^nums[i]
        i=i+2
    print(ans)
