def modulo(num):
  return num%1000000007

def number_count(current,M):
    if M is 0:
        return 1
    call=0
    for i in range(0,N):
        if current[i]+1<=size[i]:
            current[i]=current[i]+1
            call=modulo(call+number_count(list(current),M-1))
            current[i]=current[i]-1
        if current[i]-1>0:
            current[i]=current[i]-1
            call=modulo(call+number_count(list(current),M-1))
            current[i]=current[i]+1
    return call

test_cases=int(input())
for i in range(0,test_cases):
    N,M=list(map(int,input().split()))
    current=list(map(int,input().split()))
    size=tuple(map(int,input().split()))
    print(number_count(current,M))
