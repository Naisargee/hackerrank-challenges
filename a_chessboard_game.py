dic={}
dic[(1,1)]=dic[(1,2)]=dic[(2,1)]=dic[(2,2)]=False
cross=[(1,1),(1,2),(2,1),(2,2)]

while len(dic)<225:
    put=[]
    add=[(2,-1),(2,1),(-1,2),(1,2)]
    for i in cross:
        for j in add:
            if i[0]+j[0]<=15 and i[1]+j[1]<=15 and i[0]+j[0]>0 and i[1]+j[1]>0:
                dic[(i[0]+j[0],i[1]+j[1])]=True
                put.append((i[0]+j[0],i[1]+j[1]))
    put=set(put)
    temp_cross=[]
    for i in put:
        for j in add:
            if i[0]+j[0]<=15 and i[1]+j[1]<=15 and i[0]+j[0]>0 and i[1]+j[1]>0:
                if (i[0]+j[0],i[1]+j[1]) not in dic:
                    temp_cross.append((i[0]+j[0],i[1]+j[1]))
    temp_cross=set(temp_cross)
    cross=[]
    for i in temp_cross:
        count=0
        for j in add:
            if i[0]-j[0]<=15 and i[1]-j[1]<=15 and i[0]-j[0]>0 and i[1]-j[1]>0:
                if (i[0]-j[0],i[1]-j[1]) in dic and dic[(i[0]-j[0],i[1]-j[1])]==True:
                    count+=1
            else:
                count+=1
        if count==4:
            dic[(i[0],i[1])]=False
            cross.append((i[0],i[1]))
#    if len(cross)==0:
#        print("leaving : ",len(dic))
"""
print("Done ",len(dic))
print(); print();
print(sorted(dic.keys()))

print(dic[(5,2)])
print(dic[(5,3)])
print(dic[(13,14)])
print(dic[(8,8)])
"""
T=int(input())
for _ in range(T):
    m,n=map(int,input().split())
    if dic[(m,n)]==False: print("Second")
    else: print("First")
