def check(n):
  
    if n==0:
        return 1
    elif n==1:
        return 0
    odd_count = 0
    even_count = 0
    c=1
    while n:
        a = n%10
        if a==1 and c%2==1:
            odd_count+=1
        elif c%2==0 and a==1:
            even_count+=1
        n=n//10
        c+=1
    if abs(odd_count-even_count)%3==0:
        return(1)
    else:
        return(0)
        
test = int(input())
for i in range(test):
    n = int(input())
    print(check(n))
