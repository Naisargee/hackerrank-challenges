N=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr)
while len(arr)>0:
    print(len(arr))
    k=arr[0]
    i=1
    while i<len(arr) and arr[i]==k: i+=1;
    arr=arr[i:]
