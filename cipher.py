N,K=map(int,input().split())
ans=[0 for x in range(K-1)]
S=list(map(int,input()))
S_count=K-1
t=0
for n in S:
    temp=n
    t=t^ans[S_count-K]^ans[S_count-1]
    temp=temp^t
    ans.append(temp)
    S_count+=1


K=K-1
ans=ans[K:(0-K)]
for i in ans:
    print(i,end="")
#ans=str(reduce(lambda x,y: str(x)+str(y),ans,""))
