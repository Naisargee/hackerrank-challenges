N=int(input())
dic={}
order=[]
for i in range(N):
    t,d=map(int,input().split())
    if t+d in dic:
        dic[t+d].append(i)
    else:
        order.append(t+d)
        dic[t+d]=[i]
order.sort()
#print(order)
#print(dic)
for i in order:
    dic[i].sort()
    for j in dic[i]:
        print(j+1,end=" ")
