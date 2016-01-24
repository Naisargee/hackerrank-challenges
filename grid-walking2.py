d={}
def number_count(current,M):
    if (tuple(current),M) in d: return d[(tuple(current),M)]
    if M is 0:
        return 1
    call=0
    for i in range(0,N):
        if current[i]+1<=size[i]:
            current[i]=current[i]+1
            call=(call+number_count(list(current),M-1))%1000000007
            current[i]=current[i]-1
        if current[i]-1>0:
            current[i]=current[i]-1
            call=(call+number_count(list(current),M-1))%1000000007
            current[i]=current[i]+1
    d[(tuple(current),M)]=call
    return call

test_cases=int(input())
for i in range(0,test_cases):
    N,M=list(map(int,input().split()))
    current=list(map(int,input().split()))
    size=tuple(map(int,input().split()))
    glo=number_count(current,M)
    print(glo)
