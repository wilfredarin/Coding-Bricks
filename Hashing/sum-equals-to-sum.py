#a = map(int,input().split())
#a = list(map(int,input().split()))


def sum_equals_to_sum(n,A):
    hash_map = {}
    for i in range(n):
        for j in range(i+1,n):
            sum = A[i]+A[j]
            if sum in hash_map:
                cd = hash_map.get(sum)
                return 1
            else:
                hash_map[sum]=A[i],A[j]
    return 0
test = int(input())
for i in range(test):
    n = int(input())
    A = list(map(int,input().split()))
    print(sum_equals_to_sum(n,A))
    
