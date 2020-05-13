def BinarySearch(arr, key):
    """
    BinarySearch takes in two parameters: list of integers, and a search integer.
    This function will then search the the list to find a match to the search key.
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
