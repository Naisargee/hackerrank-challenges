def fact(num):
    if num is 0: return 1
    else: return num*fact(num-1)

def get_primes(start, stop):
    dct = {x: True for x in list(range(start, stop+1))}
    x = start

    while x ** 2 <= stop:
        if dct[x]:
            y = x ** 2
            while y <= stop:
                dct[y] = False
                y += x
        x += 1

    lst = []
    for x, y in dct.items():
        if y:
            lst.append(x)

    return lst

T=int(input())
for _ in range(0,T):
    N=int(input())
    i=0
    ubhi=N
    ans=0
    while i*4<=N:
        ubhi=N-i*4
        aadi=i
        temp=fact(ubhi+aadi)
        temp=temp/fact(ubhi)
        temp=temp/fact(aadi)
        ans+=temp
        i+=1
    if ans<2: print(0)
    else:
        print(len(get_primes(2,int(ans))))
