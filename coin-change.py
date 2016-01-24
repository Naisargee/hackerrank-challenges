d={}
def count_poss(coins,sum_value):
    if (tuple(coins),sum_value) in d: return d[(tuple(coins),sum_value)]
    value=coins.pop()
    if sum_value is 0:
        d[(tuple(coins),value)]=1
        return 1
    if not coins:
        d[(tuple(coins),value)]=0
        return 0
    if sum_value<value:
        d[(tuple(coins),value)]=0
        return 0
    ans=0
    while value<=sum_value:
        ans=ans+count_poss(list(coins),sum_value)
        sum_value=sum_value-value
    ans=ans+count_poss(list(coins),sum_value)
    d[(tuple(coins),value)]=ans
    return ans


N,M=map(int,input().split())
C=list(map(int,input().split()))
C.sort()
C.reverse()
print(count_poss([6,5,3,2],10))
