def BinarySearch(arr, element):
    start = 0
    end = len(arr) - 1
    middle=0
    if start <= end:
        middle = (start + end) // 2
        if arr[middle] == element:
            return middle
        if arr[middle] < element:
            return BinarySearch(arr[middle + 1:], element)
        elif arr[middle] > element:
            return BinarySearch(arr[:middle], element)

    return -1


print(BinarySearch([ 2, 3, 4, 10, 40 ,50,60,70,80], 40))

