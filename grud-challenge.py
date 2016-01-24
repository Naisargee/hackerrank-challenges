T=int(input())
for _ in range(0,T):
    N=int(input())
    G=[]
    for i in range(0,N):
        ip=list(input())
        ip.sort()
        G.append(ip)
    br=0
    for i in range(0,N):
        for j in range(0,N-1):
            if G[j][i]>G[j+1][i]:
                br=1
                break
    if br==0: print("YES")
    else: print("NO")
    #print(G)
