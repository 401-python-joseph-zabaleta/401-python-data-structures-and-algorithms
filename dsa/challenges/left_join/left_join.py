
def left_join(hashmap1, hashmap2):
    """Takes in two hash maps and left joins them. The first parameter will look the the second parameter for matching keys and get those values, if no match is found null will be return for that row in the the table. Result will be a returned combination of both.
    """
    output = []

    for key in hashmap1:
        row = []
        row.append(key)
        row.append(hashmap1[key])

        try:
            if hashmap2[key]:
                row.append(hashmap2[key])
        except:
            row.append(None)

        output.append(row)
    return output
