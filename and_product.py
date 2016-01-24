T=int(input())
for _ in range(0,T):
    S,L=map(int,input().split())
    if S==0 or L==0:
        print(0)
        continue
    S='{0:032b}'.format(S)
    L='{0:032b}'.format(L)
    S=list(S)
    L=list(L)
    S.reverse()
    L.reverse()
    s=S.pop()
    l=L.pop()
    while s!='1' and l!='1' and S:
        s=S.pop()
        l=L.pop()
    ans=[]
    if len(S)>0:
        ans.append('1')
        s=S.pop()
        l=L.pop()
        while s==l and S:
            ans.append(s)
            s=S.pop()
            l=L.pop()
        ans.append('0')
        for i in S: ans.append('0')
        print(int(''.join(ans),2))
    else:
        print(0)
