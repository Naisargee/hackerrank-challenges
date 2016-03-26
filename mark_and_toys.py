N,K=map(int,input().split())
nums=list(map(int,input().split()))

nums.sort()
count=0
so_far=0
for i in nums:
    if so_far+i<=K:
        count+=1
        so_far=so_far+i
    else:
        break
print(count)
