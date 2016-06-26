T=int(input())
for _ in range(T):
    k=list(input())
    maxi=k[-1]
    i=len(k)-2
    while i>=0 and k[i]>=maxi: maxi=k[i]; i=i-1
    if i==-1: print("no answer"); continue;
    sub=k[i+1:]
    replace=k[i+1]
    for j in sub:
        if j<replace and j>k[i]: replace=j
    sub.remove(replace)
    sub.append(k[i])
    k[i]=replace
    sub.sort()
    k=k[:i+1]+sub
    print("".join(k))
