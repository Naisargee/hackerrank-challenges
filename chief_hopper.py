N=int(input())
A=list(map(int,input().split()))

A.reverse()

k=0
for i in A:
    if (k+i)%2==0 : k=int((k+i)/2)
    else: k=int((k+i)/2)+1
print(k)
