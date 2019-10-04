# your code goes here
def is_possible(cow,array,x):
    i = 0
    j = 1
    cow =cow-1
    while j < len(array) and cow >0 :
        if array[j]-array[i]>=x:
            cow -= 1
            i = j
            j += 1
        else:
            j += 1
    if cow > 0:
        return False
    else:
        return True

def aggresive_cow(n,cow,array):

    array.sort()
    n-=1
    gap = array[n] - array[0]
    r = 0
    l = gap
    
    ans = []
    mid = (r+l)//2
    while  r <= l:
        mid = (r+l)//2
       
        if is_possible(cow,array,mid):
            
            ans.append(mid)
            r = mid+1
           
        else:
            l = mid -1 
    print(max(ans))
    
t  = int(input())
a = []
for i in range(t):
	a = []
	n,cow = map(int,input().split())
	a = list(map(int,input().split()))
	aggresive_cow(n,cow,a)
	
	
