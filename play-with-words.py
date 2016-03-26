import sys
sys.setrecursionlimit(10**7)

dic={}

def find_max_pali(string):
    if string in dic: return dic[string]
    if len(string)==0:
        dic[string]=0
        return 0
    if len(string)==1:
        dic[string]=1
        return 1
    if string[0]==string[-1]:
        if string[1:-1] in dic:
            dic[string]=2+dic[string[1:-1]]
        else:
            if len(string[1:-1])==0: dic[string]=2
            elif len(string[1:-1])==1: dic[string]=3
            else: dic[string]=2+find_max_pali(string[1:-1])
        return dic[string]
    else:
        if string[1:] in dic:
            left_max=dic[string[1:]]
        else:
            if len(string[1:])==0: left_max=0
            elif len(string[1:])==1: left_max=1
            else: left_max=find_max_pali(string[1:])
        if string[:-1] in dic:
            right_max=dic[string[:-1]]
        else:
            if len(string[:-1])==0: right_max=0
            elif len(string[:-1])==1: right_max=1
            else: right_max=find_max_pali(string[:-1])
        dic[string]=max(left_max,right_max)
        return dic[string]

def find_answer(string):
    answer=0
    for i in range(1,len(string)):
        left_max=find_max_pali(string[:i])
        right_max=find_max_pali(string[i:])
        ans= left_max*right_max
        #print(string[:i],string[i:],left_max,right_max,ans,answer,end=" ")
        if ans > answer:
            #print("updating answer")
            answer=ans
        #else: print()
    return answer

#print(find_max_pali("forskeeggeeks"))
print(find_answer(input()))
