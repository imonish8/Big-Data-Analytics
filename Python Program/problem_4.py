def diagonal_sum(matrix):
    # TODO
    sumD = 0  # Initialize the sum variable
    for i in range(len(matrix)):
        sumD += matrix[i][i]
    return sumD

# time : O(N)
# space : O(1)
