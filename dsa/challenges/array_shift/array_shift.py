## Function  
def insertShiftArray(arr, num):
    answerArr = []
    middle = 0
    # No math methods, if/else to determine odd or even to find middle index
    if len(arr) % 2 == 0:
        middle = len(arr)/2
    else:
        middle = (len(arr)/2 + 0.5)
    
    #Loop through originally arr length + 1 more iteration for our addition.
    for i in range(len(arr)+1):
        if i < middle:
            #append first half
           answerArr.append(arr[i])
        elif i == middle:
            #append parameter2 num to middle of our have list
            answerArr.append(num)
            answerArr.append(arr[i])
        elif i > middle and i < len(arr):
            #append second half
            answerArr.append(arr[i])
    return(answerArr)

# First Input
assert insertShiftArray([2,4,6,8], 5) == [2,4,5,6,8]

# Second Input
assert insertShiftArray([4,8,15,23,42], 16) == [4,8,15,16,23,42]