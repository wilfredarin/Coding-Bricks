#code
n=int(input())

def is_balanced(a):
    s = []
    o = ["[","{","("]
    c = ["]","}",")"]
    for i in a:
        if i in o:
            s.append(i)
        else:
            if not s:
                return  print("not balanced")
            e = s.pop()
            if c.index(i)!=o.index(e):
                return print("not balanced")
    if s:
        return print("not balanced")
    return print("balanced")
for i in range(n):
    a =list(input())
    is_balanced(a)
    
