N,K = map(int,input().split())

nums=list(map(int,input().split()))

dic={}
for i in range(0,N): dic[nums[i]]=i

def exchange(num1,num2):
    num1_pos=dic[num1]
    num2_pos=dic[num2]
    nums[num1_pos]=num2
    nums[num2_pos]=num1
    dic[num1]=num2_pos
    dic[num2]=num1_pos

k=0
n=0
num=N

while k<K and n<N:
    if nums[n]==num:
        n=n+1
        num=num-1
        continue
    exchange(num,nums[n])
    n=n+1
    num=num-1
    k=k+1

    #print(nums)

for i in nums: print(i,end=" ")
print()
