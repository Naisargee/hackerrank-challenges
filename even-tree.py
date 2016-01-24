class node:
    def __init__(self,val):
        self.value=val
        self.adj=[]
####taking input############
N,E=map(int,input().split())
nodes=[]
for i in range(N):
    nodes.append(node(i))
for _ in range(E):
    n1,n2=map(int,input().split())
    n1=n1-1
    n2=n2-1
    nodes[n1].adj.append(n2)
    nodes[n2].adj.append(n1)
############################

def findEdges(n):
    ans=0
    for i in nodes[n].adj:
        k=childCount(n,i)
        if k%2==0 and k!=0:
            ans=ans+1
    return ans

def childCount(p,n):
    ans=1
    for i in nodes[n].adj:
        if i is not p:
            ans=ans+childCount(n,i)
    return ans

ans=0
for i in range(N):
#    print("Node ",i)
    ans=ans+findEdges(i)
print(int(ans/2))
