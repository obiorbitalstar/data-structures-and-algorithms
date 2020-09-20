# Selection Sort
Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.


# Pseudocode

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

# Trace
Sample Array : [9,5,1,4,3]

The first element in the array is assumed to be sorted. Take the second element and store it separately in key.

Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.

* step 1:

![img](https://cdn.programiz.com/sites/tutorial2program/files/Insertion-sort-0_1.png)

If the first element is greater than key, then key is placed in front of the first element.

* step 2:
Now, the first two elements are sorted.

Take the third element and compare it with the elements on the left of it. Placed it just behind the element smaller than it. If there is no element smaller than it, then place it at the beginning of the array.

![img](https://cdn.programiz.com/sites/tutorial2program/files/Insertion-sort-1_1.png)

Place 1 at the beginning

* step 3:
Similarly, place every unsorted element at its correct position.

![img](https://cdn.programiz.com/sites/tutorial2program/files/Insertion-sort-2_2.png)
Place 4 behind 1

* step 4:

![img](https://cdn.programiz.com/sites/tutorial2program/files/Insertion-sort-3_2.png)
