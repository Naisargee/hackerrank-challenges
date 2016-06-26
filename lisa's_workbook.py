Ch,K=map(int,input().split())
arr=list(map(int,input().split()))
page_no=1
ans=0
for i in range(0,Ch):
    prob_no=1
    while prob_no<=arr[i]:
        if prob_no<=page_no and page_no<(prob_no+K):
            if page_no<=arr[i]:
                ans+=1
#                print("Adding  :",page_no,i,prob_no)
        prob_no+=K
        page_no+=1
print(ans)
