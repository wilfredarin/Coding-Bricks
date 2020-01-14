def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def partition(arr,low,high):
    #add code here
    least = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            least+=1
            arr[least],arr[j] = arr[j],arr[least]
    arr[least+1],arr[high] = arr[high],arr[least+1]
    return (least + 1)
