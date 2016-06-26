win=[0]*101

win[1]=False
win[2]=True
win[3]=True
win[4]=True
win[5]=True

for i in range(6,101):
    if win[i-5]==False or win[i-3]==False or win[i-2]==False:
        win[i]=True
    else: win[i]=False

T=int(input())
for _ in range(T):
    n=int(input())
    if win[n]==True: print("First")
    else: print("Second")
