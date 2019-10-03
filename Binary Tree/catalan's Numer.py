# catalan's Numer : 2n!/(n+1)!*n!
import math
Test = int(input())
answer = []
catalan = 0
for i in range(Test):
    number = int(input())
    catalan = (math.factorial(2*number))//((math.factorial(number+1))*(math.factorial(number)))
    answer.append(catalan)
for i in answer:
    print(i)
