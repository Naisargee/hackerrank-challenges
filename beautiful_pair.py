N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A_f=[(i,A[i]) for i in range(len(A))]
B_f=[(i,B[i]) for i in range(len(B))]

A=sorted(A_f,key=lambda x: x[1])
B=sorted(B_f,key=lambda x: x[1])
#print(A[:10])
#print()
#print(B[:20])



count=0
j=0
i=0
while i<N and j<N:
    print(A[i][1],B[j][1])
    if A[i][1]==B[j][1]:
        count=count+1
        i=i+1
        j=j+1
    elif A[i][1]<B[j][1]: i=i+1
    else: j=j+1
if(count!=N):
    print(count+1)
else:
    print(count)
