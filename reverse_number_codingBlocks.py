number = int(input())
counter = 1
digit = 0
answer = 0
while number:
	digit = number%10
	answer += counter*(10**(digit-1))

	number = number//10
	counter+=1
print(answer)
#32145 >> 12543
