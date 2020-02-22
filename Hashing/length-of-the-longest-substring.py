"""
########## length-of-the-longest-substring ################
Given a string, find the length of the longest substring without repeating characters. For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is str.

Output:

Print the length of longest substring.

Constraints:

1 ≤ T ≤ 20
1 ≤ str ≤ 50

Example:

Input:
2
geeksforgeeks
qwertqwer

Output:
7
5


######## Solution in Python ###############
"""





test = int(input())
for i in range(test):
    s = input()
    n = len(s)
    hash_table = {}
    curr_len = 1
    max_len = 1
    hash_table[s[0]]=0
    
    for i in range(1,n):
        char = s[i]
        if char not in hash_table or i-curr_len > hash_table[char]:
            curr_len+=1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = i-hash_table[char]
        hash_table[char]=i
    max_len = max(max_len,curr_len)
    print(max_len)
            
    
    
