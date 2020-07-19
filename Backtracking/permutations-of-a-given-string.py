
#https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0

def perm(a):
    cur = []
    res = []
    n = len(a)
    def help(a,cur,res,n):
        if len(cur)==n:
            res.append("".join(cur))
        else:
            for i in range(n):
                if a[i] not in cur:
                    cur.append(a[i])
                    help(a,cur,res,n)
                    cur.pop()
        return res
    return help(a,cur,res,n)
test = int(input())
for i in range(test):

    a = input()
    ans = sorted(perm(a))
    for p in ans:
        print(p,end=" ")
    print("")
        
    
