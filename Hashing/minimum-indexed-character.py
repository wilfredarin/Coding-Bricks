
#https://practice.geeksforgeeks.org/problems/minimum-indexed-character/0/
def hashTable(n,arr):
    hash_table = {}
    for i in range(n):
        if arr[i] not in hash_table:
            hash_table[arr[i]]=i
    return hash_table    
            
test = int(input())
for i in range(test):
    b = list(input())
    arr = list(input())
    n = len(arr)
    hash_map = hashTable(n,arr)
    T = 0
    for i in b:
        if i in hash_map:
            print(i)
            T = 1
            break
    if not T:
        print("$")
    
    
