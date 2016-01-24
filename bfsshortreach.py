def bfs(visit_ed,c):
    if not visit_ed: return
    k=[]
    for node in visit_ed:
        for n in neighbours[node]:
            if n not in count and n not in visit_ed:
                k.append(n)
                count[n]=c
    bfs(list(k),c+1)


test_cases=int(input())
for t in range(0,test_cases):
    V,E=list(map(int,input().split()))
    neighbours={}
    visited=[]
    count={}
    for i in range(1,V+1):
        neighbours[i]=[]
    for i in range(0,E):
        v1,v2=list(map(int,input().split()))
        neighbours[v1].append(v2)
        neighbours[v2].append(v1)
    S=int(input())
    visited.append(S)
    count[S]=0
    bfs(visited,1)

    for i in range(1,S):
        if i in count:
            print(count[i]*6,end=" ")
        else:
            print(-1,end=" ")
    for i in range(S+1,V+1):
        if i in count:
            print(count[i]*6,end=" ")
        else:
            print(-1,end=" ")
