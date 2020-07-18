https://practice.geeksforgeeks.org/problems/wildcard-pattern-matching/1
# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
def wildCard(str1, str2):
    # Code here
    str1,str2 = str2,str1
    p_l = len(str1)
    s_l = len(str2)
    dp = [[False for i in range(p_l+1)] for j in range(s_l+1)]
    dp[0][0] = True
    
    #first row
    for j in range(1,p_l+1):
        if str1[j-1]=="*":
            dp[0][j] = dp[0][j-1]
    
    #first col ->all false
    
    for i in range(1,s_l+1):
        for j in range(1,p_l+1):
            if str1[j-1] == "*":
                #left or top
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif str1[j-1] == "?" or str2[i-1] == str1[j-1]:
                #diagnol
                dp[i][j] = dp[i-1][j-1]
           
    ans = dp[-1][-1]      

    return ans
