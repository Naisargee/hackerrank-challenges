def solveThis(S,n):
    count={}
    for c in S:
        count[c]=count.get(c,0)+1

    for c in count:
        if count[c]>(n/4):
            count[c]=count[c]-int(n/4)
        else:
            count[c]=0

    count2={}

    i,j,ans=0,0,n
    while j<n:
        while j<n and any(count2.get(c,0)<count[c] for c in count):
            count2[S[j]]=count2.get(S[j],0)+1
            j+=1
        while all(count2.get(c,0)>=count[c] for c in count):
            count2[S[i]]=count2[S[i]]-1
            i+=1
        if j-i+1<ans:
            ans=j-i+1
    return ans
N=int(input())
S=input()
print(solveThis(S,N))
