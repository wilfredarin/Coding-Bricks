"""Simplify the directory path (Unix like)
Given an absolute path for a file (Unix-style), simplify it. Note that absolute path always begin with ‘/’ ( root directory ), a dot in path represent current directory and double dot represents parent directory.

Examples:

"/a/./"   --> means stay at the current directory 'a'
"/a/b/.." --> means jump to the parent directory
              from 'b' to 'a'
"////"    --> consecutive multiple '/' are a  valid  
              path, they are equivalent to single "/".

Input : /home/
Output : /home

Input : /a/./b/../../c/
Output : /c

Input : /a/..
Output:/

Input : /a/../
Output : /

Input : /../../../../../a
Output : /a

Input : /a/./b/./c/./d/
Output : /a/b/c/d

Input : /a/../.././../../.
Output:/

Input : /a//b//c//////d
Output : /a/b/c/d
By looking at examples we can see that the above simplification process just behaves like a stack.
Whenever we encounter any file’s name, we simply push it into the stack. when we come across ” . ” we do nothing.
When we find “..” in our path, we simply pop the topmost element as we have to jump back to parent’s directory.
When we see multiple “////” we just ignore them as they are equivalent to one single “/”. 
After iterating through the whole string the elements remaining in the stack is our simplified absolute path.
We have to create another stack to reverse the elements stored inside the original stack and then store the result inside a string.


"""

def simplifyPath(self, A):
        stack = []
        dir = ""
        res = ""
        res+="/"
        n = len(A)
        i = 0
        while i<n:
            #new comand
            dir_str = ""
            
            while i<n and A[i]=="/":
                i+=1
            while i<n and A[i]!="/":
                dir_str+=A[i]
                i+=1
            if dir_str==".." :
                if stack:
                    stack.pop()
            elif dir_str==".":
                continue
            elif dir_str:
                stack.append(dir_str)
            i+=1
        stack.reverse()
        while stack:
            temp = stack[-1]
            if len(stack)!=1:
                res+=temp+"/"
            else:
                res+=temp
            stack.pop()
        return res
