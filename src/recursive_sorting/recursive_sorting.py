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
    left = start
    right = mid + 1
    if arr[mid] <= arr[right]:
        return arr

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            left += 1
        else:
            # temp = arr[right]
            for i in range(left + 1, left + 1 + right - left):
                arr.insert(left, arr.pop(i))
            # arr[left] = temp
            left += 1
            mid += 1
            right += 1

    print(arr)
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l >= r:
        return arr

    merge_sort_in_place(arr, l, (l + r) // 2)
    merge_sort_in_place(arr, ((l + r) // 2) + 1, r)

    return merge_in_place(arr, l, (l+r) // 2, r)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 12, 7]

print(merge_sort_in_place(arr1, 0, len(arr1)-1))
