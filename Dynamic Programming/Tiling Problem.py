def tile(n,look):
    if look[n]:
        return look[n]
    else:
        look[n] = tile(n-1,look)+tile(n-2,look)
    return look[n]

test = int(input())
for i in range(test):
    n  = int(input())
    look = [0]*(n)
    look[0]=1
    look[1]=2
    print(tile(n-1,look))
