N=int(input())
nums=list(map(int,input().split()))
nums.sort()
print(nums)
count=1
k=nums[0]
nums=nums[1:]
for i in nums:
    if i<=k+4: continue
    count+=1
    k=i
print(count)
