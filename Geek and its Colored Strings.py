
import math
n=int(input())
for i in range(n):
    ans = 0
    n,r,g,b=map(int,(input().split()))
    l = math.factorial
    left = n-r-g-b
    for i in range(left+1):
        for j in range(left-i+1):
            k = left - i - j
            ans += (l(n)//(l(r+i)*l(g+j)*l(b+k)))
    print(ans)
    
