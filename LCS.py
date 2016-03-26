N,M=map(int,input().split())
S1=input().split()
S2=input().split()
ans=[]

dic={}
def LongestCommon(S1,S2):
#    global dic
    if len(S1)==0 or len(S2)==0:
        return []
#    if len(S2)==6 : print(S1,S2)
    original="".join(S1)
    original+="".join(S2)
#    print(original)
    if original in dic :
#        print(dic[original])
        return dic[original]
    ss1=S1.pop()
    k2= list(LongestCommon(list(S1),list(S2)))
    ss2=S2.pop()
    S1.append(ss1)
    k3 = list(LongestCommon(list(S1),list(S2)))
    ss1=S1.pop()
    k = list(LongestCommon(list(S1),list(S2)))
    if ss1==ss2:
        k.append(ss1)
    lk=len(k)
    lk2=len(k2)
    lk3=len(k3)
#    print(lk3,lk2,lk)
    if lk2>=lk3 and lk2>=lk:
#        print(k3)
        dic[original]=list(k2)
        return list(k2)
    if lk3>=lk2 and lk3>=lk:
#        print(k2)
        dic[original]=list(k3)
        return list(k3)
    dic[original]=list(k)
#    print(k)
    return list(k)



ans=LongestCommon(S1,S2)
op=""
for x in ans : op=op+str(x)+" "
print(op)
#print(dic)
