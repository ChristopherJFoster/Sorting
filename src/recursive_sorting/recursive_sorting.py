# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    for _ in range(len(arrA) + len(arrB)):
        if len(arrA) > 0:
            if len(arrB) > 0:
                if arrA[0] < arrB[0]:
                    merged_arr.append(arrA.pop(0))
                else:
                    merged_arr.append(arrB.pop(0))
            else:
                return merged_arr + arrA
        else:
            return merged_arr + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print(arr)
    # TO-DO

    if len(arr) > 1:
        merge_sort([arr[i] for i in range(0, len(arr)) if i < len(arr) // 2])
        merge_sort([arr[i] for i in range(0, len(arr)) if i >= len(arr) // 2])

    return arr


arr = [5, 1, 2, 1, 0]

# print(merge_sort(arr))

arrA = [1, 3, 6, 90]
arrB = [23, 24, 100]
print(merge(arrA, arrB))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
