#egg-dropping-puzzle
#a = list(map(int,input().split()))

def egg(f,e):
    a = [[0 for i in range(f+1)] for j in range(e+1)]
    for i in range(1,f+1):
        a[1][i]=i

    for egg in range(2,e+1):
        for floor in range(1,f+1):
            l = 10000000
            for k in range(1,floor+1): 
                s =1+ max(a[egg-1][k-1],a[egg][floor-k])
                l = min(s,l)
                    
            a[egg][floor] = l
    return a[-1][-1]
test = int(input())
for i in range(test):
    f,e = map(int,input().split())
    a = egg(e,f)
    print(a)
