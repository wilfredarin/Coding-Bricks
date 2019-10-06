test = int(input())
for i in range(test):
    n = int(input())
    l = list(map(int,(input().split())))
    s = []
    ans = []
    for i in range(n-1,-1,-1):
        cur = l[i]
        if s and s[-1]>cur:
            ans.append(str(s[-1]))
            
        else:
            while s and s[-1]<cur:
                s.pop()
            if s and s[-1]>cur:
                ans.append(str(s[-1]))
            if not s:
                ans.append("-1")
            
        s.append(cur)       
    ans.reverse()
    print(" ".join(ans))
        
    	
        
