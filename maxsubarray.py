t=int(input())
while t is not 0:
    N=int(input())
    arr=list(map(int,input().split()))
    tot_max=arr[0]
    cur_max=arr[0]
    ans2=arr[0]
    for i in range(1,N):
        k=arr[i]+cur_max
        cur_max=max(k,arr[i])
        if cur_max>tot_max: tot_max=cur_max
        ans2=max(ans2,arr[i],ans2+arr[i])
    print(tot_max,"  ",ans2)
    t=t-1
