T=int(input())
for _ in range(0,T):
    M=int(input())
    N=int(input())
    prices={}
    temp=list(map(int,input().split()))
    for i in range(0,len(temp)):
        if temp[i] in prices:
            prices[temp[i]].append(i+1)
        else:
            prices[temp[i]]=[i+1]
    index1=0
    index2=0
    for i in temp:
        if M<i: continue
        index1=prices[i][0]
        p2=M-i
        if p2!=i:
            if p2 in prices:
                index2=prices[p2][0]
                break
        else:
            if len(prices[i])>=2:
                index2=prices[i][1]
                break
    print(index1,index2)
    print(temp[index1-1],temp[index2-1])
