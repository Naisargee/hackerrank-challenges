T=int(input())
for _ in range(0,T):
    M,N=map(int,input().split())
    M_cut=1
    N_cut=1
    M_list=list(map(int,input().split()))
    N_list=list(map(int,input().split()))
    M_list.sort()
    N_list.sort()
    cost=0
    while M_list and N_list:
        m=M_list.pop()
        n=N_list.pop()
        if m>n:
            N_list.append(n)
#            print("addind_cost",m*N_cut)
            cost+=m*N_cut
            M_cut+=1
        else:
            M_list.append(m)
#            print("addind_cost",n*M_cut)
            cost+=n*M_cut
            N_cut+=1
    if M_list:
        for i in M_list:
#            print("addind_cost",i*N_cut)
            cost+=i*N_cut
    if N_list:
        for i in N_list:
#            print("addind_cost",i*M_cut)
            cost+=i*M_cut
    print(cost)
