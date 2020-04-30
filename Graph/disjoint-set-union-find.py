#https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1
def find(arr, x):
    # Code here
    if arr[x-1] == x:
        return arr[x-1]
    else:
        return find(arr,arr[x-1])
    

# function shouldn't return or print anything
def union(arr, x, z):
    # Code here
    x_parent = find(arr, x)
    z_parent = find(arr, z)
    if x_parent == z_parent:
        return
    else:
        arr[x_parent-1] = z_parent
