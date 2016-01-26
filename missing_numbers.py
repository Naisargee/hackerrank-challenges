N=int(input())
arrayA=list(map(int,input().split()))
M=int(input())
arrayB=list(map(int,input().split()))
if M==N:
    print()
else:
    dA={}
    for k in arrayA:
        if k in dA: dA[k]+=1
        else: dA[k]=1
    dB={}
    for k in arrayB:
        if k in dB: dB[k]+=1
        else: dB[k]=1
    ans=[]
    for k in dB:
        if k not in dA:
            ans.append(k)
            continue
        if dB[k]>dA[k]:
            ans.append(k)
    for x in ans: print(x,end=" ")
