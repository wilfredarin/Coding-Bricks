def maxLen(n, arr):
    #Code here
    hash_map = {0:-1}
    max_len = 0
    cur_sum = 0
    for i in range(n):
        cur_sum += arr[i]
        if cur_sum not in hash_map:
            hash_map[cur_sum]=i

        if cur_sum in hash_map:
            if i-hash_map[cur_sum]>max_len:
                max_len = i-hash_map[cur_sum]
    return max_len
