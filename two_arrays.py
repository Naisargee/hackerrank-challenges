T=int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A_nums=list(map(int,input().split()))
    B_nums=list(map(int,input().split()))
    A_nums.sort()
    B_nums.sort()
    B_nums.reverse()
    ans=[A_nums[i]+B_nums[i] for i in range(0,N)]
    decision=0
    for i in ans:
        if i<K:
            decision=1
            break
    if decision==0: print("YES")
    else: print("NO")
