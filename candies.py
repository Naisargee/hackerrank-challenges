N=int(input())
ranks=[]
for _ in range(0,N):
    t=int(input())
    ranks.append(t)
candies=[1 for x in range(0,len(ranks))]
for i in range(1,len(ranks)):
    if ranks[i-1]<ranks[i]:
        candies[i]=candies[i-1]+1
    elif ranks[i-1]>ranks[i]:
        j=i
        while ranks[j-1]>ranks[j]:
            candies[j-1]=max(candies[j-1],candies[j]+1)
            j=j-1
    else:
        candies[i]=1
ans=0
for i in candies:
    ans=ans+i
print(ans)
