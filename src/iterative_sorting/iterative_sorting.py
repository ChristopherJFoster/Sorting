# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(list):
    swap = True
    # loop will keep running until a no-swap pass through the list is completed
    while swap == True:
        for i in range(1, len(list)):
            if i == 1:
                # resets swap tracker to False at the beginning of each pass through list
                swapped = False
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
                # if a swap occurs on this particular comparison, the pass gets credit for a swap
                swapped = True
        # when a no-swap pass is complete, this will "tell" the while loop to stop running
        swap = swapped
    return list


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(bubble_sort(nums))
