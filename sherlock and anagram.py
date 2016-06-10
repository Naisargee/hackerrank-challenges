def findAnswer(string,count):
    if len(string)<=count:
        return 0
    substrings=[]
    for i in range(0,len(string)-count+1):
        substrings.append(string[i:i+count])
#    print(substrings)
    ans=0
    for i in range(0,len(substrings)):
        for j in range(i+1,len(substrings)):
            match_found=1
#            print(substrings[i],substrings[j])

            for c in set(substrings[i]):
                if substrings[i].count(c)!=substrings[j].count(c):
#                    print("broke")
                    match_found=0
                    break
            if match_found==1:
#                print("added")
                ans+=1
    return ans

T=int(input())

for _ in range(T):
    string=input()
    ans=0
    for i in range(1,len(string)):
        ans+=findAnswer(string,i)
    print(ans)
