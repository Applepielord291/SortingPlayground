# Insertion sort
def Sort(arr):
    n = len(arr)
    i = 1
    while i < n:
        x = arr[i]
        j = i-1
        while j >= 0 and x < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
        i += 1
    return arr
