def quick_sort(alist, left, right):
    if left < right:
        # Partition the array by setting the position of the pivot value
        position = partition(alist, left, right)
        # Sort the left
        quick_sort(alist, left, position - 1)
        # Sort the right
        quick_sort(alist, position + 1, right)

def partition(alist, left, right):
    # set a pivot value as a point of reference
    pivot = alist[right]
    # create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1

    for i in range(left, right):
        if alist[i] <= pivot:
            low += 1
            swap(alist, i, low)

    # place the vaue of the pivot location in the middle
    # all numbers smaller than the pivot are on the left, larger on the right.
    swap(alist, right, low + 1)
    # return the pivot index point
    return low + 1

def swap(alist, i, low):
    temp = alist[i]
    alist[i] = alist[low]
    alist[low] = temp
