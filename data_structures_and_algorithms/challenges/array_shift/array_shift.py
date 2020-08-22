def insert_shift_array(arr,n):
    if n == None:
        return arr
    if len(arr)==0:
        arr.append(n)
        return arr
    for i in range(len(arr)):
        if arr[i] > n:
            index = i
            break
    arr = arr[:i] + [n] + arr[i:]
    return arr



