N,M = map(int,input().split())
STRINGS=[]
for i in range(N):
    k=input()
    if len(k)<=M:
        STRINGS.append(k)

def modulo(num) : return num%(10**9+7)
dic={}

def hyperStrings(length):
    #print(length)
    if length<0: return 0
    if length in dic : return dic[length]
    global STRINGS
    ans=1
    for i in STRINGS:
        ans=modulo(ans+hyperStrings(length-len(i)))
    dic[length]=ans
    return ans

ANS=hyperStrings(M)
print(ANS)
