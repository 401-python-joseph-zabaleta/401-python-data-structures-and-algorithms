def merge_sort(list_arg):

    n = len(list_arg)

    if n > 1:
        mid = n // 2
        left = list_arg[:mid]
        right = list_arg[mid:]

        # sort the left side
        merge_sort(left)

        # sort the right side
        merge_sort(right)

        # Merge the sorted left and right sides together
        merge(left, right, list_arg)

def merge(left, right, list_arg):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list_arg[k] = left[i]
            i += 1
        else:
            list_arg[k] = right[j]
            j += 1

        k += 1

    # Remaining values

    while i < len(left):
        list_arg[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        list_arg[k] = right[j]
        j += 1
        k += 1


