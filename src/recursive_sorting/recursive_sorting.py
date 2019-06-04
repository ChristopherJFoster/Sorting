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
    # TO-DO
    if len(arr) <= 1:
        return arr

    arrA = [arr[i] for i in range(len(arr)) if i < len(arr) // 2]
    arrB = [arr[i] for i in range(len(arr)) if i >= len(arr) // 2]

    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    return merge(arrA, arrB)


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
