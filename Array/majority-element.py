#https://practice.geeksforgeeks.org/problems/majority-element/0
#a = map(int,input().split())
#a = list(map(int,input().split()))

def findPossible(n,a):
    count = 1
    cur_e = a[0]
    for i in range(1,n):
        if a[i]==cur_e:
            count+=1
        else:
            count-=1
            if count==0:
                count=1
                cur_e = a[i]
    return cur_e

def isMost(n,a,e):
    count = 0
    for i in range(n):
        if a[i]==e:
            count+=1
        if count>n//2:
            return e
    return -1
            
        
    
    
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int,input().split()))
    e = findPossible(n,a)
    print(isMost(n,a,e))
    
