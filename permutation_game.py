dic={}
for i in range(1,16):
    dic[str(i)]=0


def check_ans(nums):
    if len(nums)==1: return 0
    if str(nums) in dic: return dic[str(nums)]
    if str(sorted(nums))==str(nums):
        dic[str(sorted(nums))]=0
        return 0
    for i in range(len(nums)):
        if check_ans(list(nums[:i]+nums[i+1:]))==0:
            dic[str(nums)]=1
            return 1
    dic[str(nums)]=0

    return 0

T=int(input())
for _ in range(T):
    N=int(input())
    nums=list(map(int,input().split()))
    if check_ans(nums)==1: print("Alice")
    else: print("Bob")
