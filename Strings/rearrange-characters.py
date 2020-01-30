test = int(input())
for i in range(test):
    n = list(input())
    l = len(n)
    n.sort()
    dic = {}
    m  =0
    for i in n:
        if i not in dic:
            dic[i]=n.count(i)
            m = max(dic[i],m)
    if m > (l)//2:
        print(0)
    else:
        print(1)
