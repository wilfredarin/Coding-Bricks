#https://practice.geeksforgeeks.org/problems/total-decoding-messages/0
#a = map(int,input().split())
#a = list(map(int,input().split()))

test = int(input())
for i in range(test):
    n = int(input())
    s = input()
    if s[0]=="0":
        print(0)
    else:

        count = [0]*(n+1)
        count[1] = 1
        count[0] = 1
        for i in range(2,n+1):
            count[i] = 0
            if s[i-1]>"0":   #just second char char
                count[i] = count[i-1]
            if s[i-2]=="1" or (s[i-2]=="2" and s[i-1]<"7"):#First tw char
                count[i] += count[i-2]
            
        print(count[n])
    
