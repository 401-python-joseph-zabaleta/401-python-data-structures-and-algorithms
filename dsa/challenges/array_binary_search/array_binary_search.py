# def BinarySearch(arr, key):
#     """
#     BinarySearch takes in two parameters: list of integers, and a search integer.
#     This function will then search the the list to find a match to the search key.
#     """
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1


def BinarySearch(arr, key):
    """
    BinarySearch takes in two parameters: list of integers, and a search integer.
    This function will then search the the list to find a match to the search key.
    """
    if len(arr) == 0:
        return -1

    if arr[len(arr) - 1] < key:
        return -1
    else:
        start_idx = 0
        end_idx = len(arr) - 1

        while start_idx <= end_idx:
            middle_idx = (start_idx + end_idx) // 2

            if arr[middle_idx] == key:
                return middle_idx
            else:
                if key < arr[middle_idx]:
                    end_idx = middle_idx - 1
                else:
                    start_idx = middle_idx + 1
    return -1
