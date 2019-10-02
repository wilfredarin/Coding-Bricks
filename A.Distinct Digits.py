n,m = map(int,input().split())
for i in range(n,m+1):
	Flag = True
	a = [0,0,0,0,0,0,0,0,0,0]
	for j in str(i):
		a[int(j)]+=1
	for k in a:
		if k>1:
			Flag = False
			break
	if Flag:
		print(i)
		exit()
print(-1)
