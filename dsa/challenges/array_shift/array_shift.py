## Function
def insertShiftArray(arr, num):
    """
    This function takes in two parameters: a list, and an integer. insertShiftArray will place the integer at the middle index of the list provided.
    """
    answerArr = []
    middle = 0
    # No math methods, if/else to determine odd or even to find middle index
    if len(arr) % 2 == 0:
        middle = len(arr) / 2
    else:
        middle = len(arr) / 2 + 0.5

    # Loop through originally arr length + 1 more iteration for our addition.
    for i in range(len(arr) + 1):
        if i < middle:
            # append first half
            answerArr.append(arr[i])
        elif i == middle:
            # append parameter2 num to middle of our have list
            answerArr.append(num)
            answerArr.append(arr[i])
        elif i > middle and i < len(arr):
            # append second half
            answerArr.append(arr[i])
    return answerArr
