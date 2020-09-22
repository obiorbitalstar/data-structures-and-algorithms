def partition(arr, low, right):
    i = (low-1)
    pivot = arr[right]

    for j in range(low, right):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i+1)

def quick_sort(arr, left, right):
    if len(arr)==0:
        return f'This list is empty'

    if len(arr) == 1:
        return arr
    if left < right:
        postion = partition(arr, left, right)
        quick_sort(arr, left, postion-1)
        quick_sort(arr, postion+1, right)

arr = [8,4,23,42,16,15]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)

