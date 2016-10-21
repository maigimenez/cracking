def zero_matix(matrix):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows, zero_cols = [], []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_cols.append(j)

    zeroed_matrix = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        if i not in zero_rows:
            for j in range(cols):
                if j in zero_cols:
                    zeroed_matrix[i][j] = 0
                else:
                    zeroed_matrix[i][j] = matrix[i][j]
    return zeroed_matrix