N=0
K=0
ANS=0
dic={}
def knapsack(nums,sumtillnow):
    global ANS
    global K
    if (str(nums),sumtillnow) in dic: return
    dic[(str(nums),sumtillnow)]=0
    if not nums:
        if (K-sumtillnow) < (K-ANS): ANS=sumtillnow
        return
    num=nums[0]
    while sumtillnow<=K:
        knapsack(list(nums[1:]),sumtillnow)
        sumtillnow=sumtillnow+num

T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    ANS=0
    dic={}
    nums=list(set(list(map(int,input().split()))))
    knapsack(nums,0)
    print(ANS)
