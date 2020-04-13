#https://practice.geeksforgeeks.org/problems/word-break-part-2/0
def wordBreak(dic,index,word,ans,res):
    if index==len(word):
        res.append(" ".join(ans))
        return res
    for j in range(index+1,len(word)+1):
        if word[index:j] in dic:
            ans.append(word[index:j])
            wordBreak(dic,j,word,ans,res)
            ans.pop()
    return res
test = int(input())
for i in range(test):
    q = int(input())
    dic = list(input().split())
    b = input()
    ans = []
    res =[]
    wordBreak(dic,0, b, ans,res)
    res.sort()
    for i in res:
        print("("+i+")",end="")
    print("")
    
