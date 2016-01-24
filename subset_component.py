from itertools import chain,combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsets(s):
    return list(map(list, powerset(s)))
dic={}
def find_group(num):
    s='{0:064b}'.format(num)
    ch='1'
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_ans(items):
    groups=[]
    for i in items:
        k=dic[i]
        br=0
        for j in groups:
            c =[val for val in j if val in k]
            if len(c)>0:
                j.extend(k)
                br=1
                break
        if br==0:
            groups.append(k)
    ans=0
    for i in groups:
        ans+=(len(set(i))-1)
    return 64-ans

n=int(input())
ip=list(map(int,input().split()))
for i in ip:
    dic[i]=find_group(i)
ans=0
for item in subsets(ip):
#    print("subset is : ",item)
    ans+=find_ans(item)
print(ans)
