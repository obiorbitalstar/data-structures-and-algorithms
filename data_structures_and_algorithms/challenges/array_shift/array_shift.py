def insertShiftArray(arr,n):
    for i in range(len(arr)):
        if arr[i] > n:
            index = i
            break
    arr = arr[:i] + [n] + arr[i:]
    return arr



