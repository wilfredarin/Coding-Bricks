#https://practice.geeksforgeeks.org/problems/longest-prefix-suffix/0
def createTable(p):
    n = len(p)
    table = [0]*n
    i = 1 
    j = 0
    while i<n:
        if p[i]==p[j]:
            j+=1
            table[i] = j
            i+=1
        else:
            if j==0:
                table[i] = 0
                i+=1
            else:
                j = table[j-1]
    return table
test = int(input())
for i in range(test):
    p = input()
    print(max(createTable(p)))
    
