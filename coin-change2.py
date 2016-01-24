d={}
def find_possibilities(coins,sum_value):
    coins.append(sum_value)
    k=""
    k=k.join(map(str,coins))
    if k in d : return d[k]
    coins.pop()
    if sum_value==0: return 1
    if len(coins)==0:
        #print("returned")
        return 0
    current_coin=coins[0]
    ans=find_possibilities(list(coins[1:]),sum_value)
    while current_coin<=sum_value:
        sum_value=sum_value - current_coin
        ans=ans + find_possibilities(list(coins[1:]),sum_value)
    d[k]=ans
    return ans

N,M=map(int,input().split())
coins=list(map(int,input().split()))
coins.sort()
print(find_possibilities(coins,N))
