def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        l  = r = p = 0
        while l<len(L) and r<len(R):
            if L[l] < R[r]:
                arr[p] = L[l]
                l += 1
            else:
                arr[p] = R[r]
                r += 1
            p+=1
        while l < len(L):
            arr[p] = L[l]
            l+= 1
            p+= 1
        while r < len(R):
            arr[p] = R[r]
            r+=1
            p+=1
