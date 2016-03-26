def ring_to_matrix():
    nrings=int(min(M,N)/2)
    matrix=[]
    for i in range(M):
        l=[]
        for i in range(N):
            l.append(0)
        matrix.append(l)
    for i in range(nrings):
        rings[i].reverse()
        spx,spy=i,i
        while spy<(N-i):
            matrix[spx][spy]=rings[i].pop()
            spy+=1
        spy-=1
        spx+=1
        while spx<(M-i):
            matrix[spx][spy]=rings[i].pop()
            spx+=1
        spx-=1
        spy-=1
        while spy>=i:
            matrix[spx][spy]=rings[i].pop()
            spy-=1
        spy+=1
        spx-=1
        while spx>i:
            matrix[spx][spy]=rings[i].pop()
            spx-=1
    return matrix
def rotate_rings(r_count):
    c=0
    print(rings)
    for i in rings:
        k=len(i)
        k=r_count%k
        r1=i[:k]
        r2=i[k:]
        rings[c]=list(r2+r1)
        c+=1


def find_rings():
    nrings=int(min(M,N)/2)
    global rings
    rings=[[] for x in range(nrings)]
    for i in range(nrings):
        spx,spy=i,i
        while spy<(N-i):
            rings[i].append(matrix[spx][spy])
            spy+=1
        spy-=1
        spx+=1
        while spx<(M-i):
            rings[i].append(matrix[spx][spy])
            spx+=1
        spx-=1
        spy-=1
        while spy>=i:
            rings[i].append(matrix[spx][spy])
            spy-=1
        spy+=1
        spx-=1
        while spx>i:
            rings[i].append(matrix[spx][spy])
            spx-=1

M,N,R=map(int,input().split())
matrix=[]
for i in range(M): matrix.append(list(map(int,input().split())))

find_rings()
print(rings)
rotate_rings(R)
print(rings)
matrix=ring_to_matrix()
for i in matrix:
    for j in i: print(j,end=" ")
    print()
