def maxSubArraySum(a,size): 
	
	max_so_far = a[0]
	max_ending_here = a[0]
	for i in range(1, size): 
		max_ending_here = max(a[i],max_ending_here + a[i])
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
	return max_so_far
test = int(input())
for i in range(test):
    size = int(input())
    a = list(map(int,input().split()))
    print(maxSubArraySum(a,size))
    
