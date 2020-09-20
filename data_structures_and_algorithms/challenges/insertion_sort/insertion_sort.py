def insertion_sort(arr):
    """
    takes an array of any length and returns it sorted in ascending order (from the least to the greatest)


    Args:
        arr : a list of any length

    Returns:
        list: a sorted list in ascending order
    """
    if len(arr)==0:
        return f'This list is empty'

    for i in range(1,len(arr)):
        j = i - 1
        temp = arr[i]
        while j>= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1]= temp
    return arr


x = [20,18,12,8,5,-2]

print(insertion_sort(x))

