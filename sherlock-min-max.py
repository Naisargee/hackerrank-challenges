N=int(input().strip())
arr=sorted(list(map(int,input().strip().split())))
P,Q=map(int,input().strip().split())

print("Array is :",arr)
ans=[]
if P<arr[0]: ans.append((P,arr[0]-P))

for i in range(1,N):
    if P<arr[i]:
        mid=(arr[i-1]+arr[i])//2
        print("Mid is : ",mid)
        if mid<=Q: ans.append((mid,mid-arr[i-1])); continue;
        else: ans.append((Q,Q-arr[i-1])); break;

if Q>arr[-1]: ans.append((Q,Q-arr[-1]))
print("Answer is :",ans)
print(max(ans,key=lambda x:x[1])[0])
