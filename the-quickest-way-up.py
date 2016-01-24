def findLength():
    visied=[]
    stack=[]
    stack.append(1)
    length=0
#    print(stack)
    while stack and 100 not in stack:
#        print(stack)
        length=length+1
        next_stack=[]
        for j in stack:
            if j not in visied:
                visied.append(j)
                for i in range(1,7):
                    if j+i<= 100 : next_stack.append(board[j+i])
            stack=list(next_stack)
    if not stack: return -1
    return length


t=int(input())
while t is not 0:
    board={i:i for i in range(1,101)}
#    print(board)
    N=int(input())
    for i in range(0,N):
        s,e=map(int,input().split())
        board[s]=e
#    N=int(input())
#    for i in range(0,N):
#        s,e=map(int,input().split())
#        board[s]=e
    M=int(input())
    for i in range(0,M):
        s,e=map(int,input().split())
        board[s]=e
#    print(board)
    print(findLength())
    t=t-1
