T=int(input())
for _ in range(0,T):
    N=int(input())
    nums=list(map(int,input().split()))
    tot_sum=0
    for i in nums:
        tot_sum+=i
    left_sum=0
    right_sum=tot_sum
    ans=0
    for i in nums:
        right_sum=right_sum-i
        if left_sum==right_sum:
            ans=1
            break
        else:
            left_sum=left_sum+i
    if ans==1 : print("YES")
    else: print("NO")
