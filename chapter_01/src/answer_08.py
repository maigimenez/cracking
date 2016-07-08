def zero_matix(matrix):
    if matrix:
        rows = [False]*len(matrix)
        cols = [False]*len(matrix[0])
        for i in range(len(rows)):
            for j in range(len(cols)):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        return matrix
    return False
