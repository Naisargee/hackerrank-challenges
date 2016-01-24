def eliminate(d,maximum,vertexs,edges):
    for k in range(T):
        mini=d[maximum][0]
        for l in d[maximum]:
            if len(d[l])<len(d[mini]):
                mini=l
        d[maximum].remove(mini)
        vertexs.remove(mini)
    vertexs.remove(maximum)
    e=[]
    for i in edges:
        if i[0] in vertexs and i[1] in vertexs:
            e.append([i[0],i[1]])
#    print(vertexs,e)
    return vertexs,e

def remove_vertex(vertexs,edges):
    if not vertexs: return 0
    if not edges: return len(vertexs)
    d={}
    for k in vertexs:
        d[k]=[]
    maximum=vertexs[0]
    for e in edges:
#        print(e[0],e[1])
        d[e[0]].append(e[1])
        d[e[1]].append(e[0])
    ans=0
    for k in vertexs:
        if d[k] is 0:
                ans+=1
                vertexs.remove(k)
        if len(d[k])>len(d[maximum]):
            maximum=k
#    print("ans is ,",ans)
    if len(d[maximum])>T:
        vertexs,edges=eliminate(d,maximum,vertexs,edges)
        ans+=remove_vertex(vertexs,edges)
#    print(vertexs,edges,ans)
    return ans


t=int(input())
for _ in range(t):
    N,T,M=map(int,input().split())
    edges=[]
    vertexs=[]
    for i in range(N):
        vertexs.append(i+1)
    for _ in range(M):
        v1,v2=map(int,input().split())
        edges.append([v1,v2])
    ans=remove_vertex(vertexs,edges)
    print(N-ans)
