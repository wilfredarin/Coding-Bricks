#https://practice.geeksforgeeks.org/problems/find-the-largest-rectangle-of-1s-with-swapping-of-columns-allowed/0
#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
for i in range(test):
    r,c = map(int,input().split())
    a = list(map(int,input().split()))
    h = [[0 for j in range(c)] for i in range(r)]
    for i in range(r*c):
        k = (i)//c
        l = (i)%c
        h[k][l] = a[i]
    
    hist = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if h[i][j]==0:
                hist[i][j] = 0
            else:
                if i==0:
                    hist[i][j] = h[i][j]
                else:
                    hist[i][j] = hist[i-1][j]+1

    for i in range(r):
        hist[i] = sorted(hist[i],reverse = True)
    
    max_area = 0
    for i in range(r):
        for j in range(c):
            max_area = max(hist[i][j]*(j+1),max_area)
    print(max_area)
                
