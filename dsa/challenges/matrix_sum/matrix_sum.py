def matrix_sum(matrix):
    """
    Matrix_sum: has one required parameter of a matrix (an array of arrays). This function will then
    sum the total of each row or each array within the matrix and return the results per row as a
    single array.
    """
    output = []
    for i in range(len(matrix)):
        counter = 0
        for j in range(len(matrix[i])):
            counter += matrix[i][j]
        output.append(counter)
    return output
