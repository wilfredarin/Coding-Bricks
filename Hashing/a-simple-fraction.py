"""
Given a fraction. Convert it into a decimal. So simple :P

eg.
10/2 = 5
3/5 = 0.6

(The Question Begins Now)  :D
If the decimals are repeating recursively, then enclose them inside  ().

eg.
8/3 = 2.(6)

as 8/3 = 2.66666666.......  infinitly.   
  

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is an integer N denoting the numerator of fraction.
The second line of each test case is an integer D denoting the denominator of fraction.

Output:

Print decimal of that fraction in separate line for each test case.

Constraints:

1 ≤ T ≤ 100
1 ≤ N,D ≤ 2000

Example:

Input
2
4
2
8
3
Output
2
2.(6)

"""

test = int(input())
for i in range(test):
    n = int(input())
    d = int(input())
    sign = n*d<0
    n = abs(n)
    d = abs(d)
    ans=""
    if sign:
        ans+="-"
    integer=n//d    
    ans+=str(integer)
    remainder = n%d
    if not remainder:
        print(ans)
    else:
        res = "."
        hash_table = {}
        flag = False
        while remainder!=0:
            if remainder in hash_table:
                index = hash_table[remainder]
                ans+= res[:index]
                ans+="("
                ans+=res[index:]
                ans+=")"
                print(ans)
                flag = True
                break
            else:
                hash_table[remainder] = len(res)
            remainder*=10
            res+=str(remainder//d)
            remainder = remainder%d
        if not flag:
            print(ans+res)
