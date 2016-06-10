T=int(input())
for _ in range(T):
    N=list(bin(int(input()))[2:])
    ones=0
    zeros=0
    for d in N:
        if d=='1':
            ones+=1
            zeros=0
        else:
            zeros+=1
    ans=ones+zeros
    if ans%2==1 : print('Richard')
    else :  print('Louise')
