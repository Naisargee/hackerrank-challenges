dic={}
def find_solution(arr):
#    print(arr)
    if len(arr)==0: return 0
    if len(arr)==1: return 1
    st="".join(map(str,arr))
    if st in dic: return dic[st]
    smallest=10**6
    while len(arr)>0:
        last=arr[0]
        sub=arr[0]
        del arr[0]
        count=1
        i=0
        while i<len(arr):
            if arr[i]<last: break
            count+=1
            last=arr[i]
            arr[i]-=sub
            if arr[i]==0: del arr[i]
            else : i=i+1

        smallest=min(smallest,count)
    dic[st]=smallest
    return smallest

T=int(input().strip())
for _ in range(T):
    arr=list(map(int,input().strip().split()))[1:]
    arr.sort()
    if len(arr)==0: print(0); continue;
    smallest=10**6
    arr2=[]
    k=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]: k=k+1
        else:
            arr2.append(k)
            if arr[i]!=(arr[i-1]+1):
                arr2_reverse=list(arr2)
                arr2_reverse.reverse()
                smallest=min(smallest,max(find_solution(arr2),find_solution(arr2_reverse)))
                arr2=[]
            k=1
    arr2.append(k)
    arr2_reverse=list(arr2)
    arr2_reverse.reverse()
    if len(arr2)>0:smallest=min(smallest,max(find_solution(arr2),find_solution(arr2_reverse)))
    print(smallest)
