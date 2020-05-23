#https://practice.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1
def Search(In, Post, InS, InE,data):
    for i in range(InS, InE+1):
        if In[i]==data:
            return i
def help(In,Post,InS, InE, postIndex):
    if InS>InE:
        return None
    node = Node(Post[postIndex[0]])
    postIndex[0]-=1
    if InS == InE:
        return node
    Iind = Search(In, Post,InS, InE, node.data)
    node.right = help(In, Post, Iind+1,InE,postIndex)
    node.left = help(In, Post, InS, Iind-1,postIndex)
    return node
def buildTree(In, post, n):
    return help(In,post,0,n-1,[n-1])
