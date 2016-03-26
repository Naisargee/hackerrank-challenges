T=int(input())
OUTPUT="NO"
N=0
def workOnRow1(r1,r2,index):
    global N
    if index>=N:
        workOnRow2(list(r2))
        return
    if r1[index]==1 :
        workOnRow1(list(r1),list(r2),index+1)
        return
    r1[index]=1
    if index+1<N and r1[index+1]==0:
        r1[index+1]=1
        workOnRow1(list(r1),list(r2),index+2)
        r1[index+1]=0
    if index-1>=0 and r2[index-1]==0:
        r2[index-1]=1
        workOnRow1(list(r1),list(r2),index+1)
        r2[index-1]=0
    if r2[index]==0:
        r2[index]=1
        workOnRow1(list(r1),list(r2),index+1)


def workOnRow2(r2):
    global N
    global OUTPUT
    i=0
    while i<N:
        if r2[i]==0:
            if i+1<N:
                if r2[i+1]!=0: return
                else: i=i+1
            else:
                return
        i=i+1
    OUTPUT="YES"

for _ in range(T):
    N = int(input())
    row1=list(map(int,input()))
    row2=list(map(int,input()))
    workOnRow1(list(row1),list(row2),0)
    print(OUTPUT)
    OUTPUT="NO"
