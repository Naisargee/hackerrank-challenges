CITIES,MACHINES_COUNT=map(int,input().split())
roads=[[] for i in range(0,CITIES)]
for i in range(0,CITIES-1):
    v1,v2,w=map(int,input().split())
    roads[v1].append((v2,w))
    roads[v2].append((v1,w))

machines=[]
for i in range(0,MACHINES_COUNT):
    machines.append(int(input()))
#roads=[[(1,5)],[(0,5),(2,8),(3,1)],[(1,8),(4,5),(5,1)],[(1,1),(6,2)],[(2,5)],[(2,1)],[(3,2)]]
#machines=[0,2,4,6]

mini_v1=0
mini_v2=0
remove=[]
def DFS(x,minimum,mini_v1,mini_v2,visited):
    if x in visited: return
    visited.append(x)
#    print("x is : ",x)
    for i in roads[x]:
        if i[0] not in visited:
            if i[1] < minimum:
                minimum=i[1]
                mini_v1=x
                mini_v2=i[0]
            if i[0] in machines:
#                print("appending ",x,i[0],mini_v1,mini_v2,visited)
                remove.append((mini_v1,mini_v2,minimum))
                DFS(i[0],9999999,-1,-1,list(visited))
            else:
                DFS(i[0],minimum,mini_v1,mini_v2,list(visited))
        if x in machines:
            minimum=9999999
            mini_v1=-1
            mini_v2=-1
    return

DFS(machines[-1],9999999,-1,-1,[])
#print(remove)
ans=0
for i in remove:
    ans+=i[2]
print(ans)
