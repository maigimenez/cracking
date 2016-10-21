def rotate_matrix(m):
    if not m:
        return []

    rows = len(m)
    # cols = len(m[0])
    # rotated_matrix = [[0]*cols for _ in range(rows)]
    # for i in range(rows):
    #     for j in range(cols):
    #         rotated_matrix[j][rows-i-1] = m[i][j]
    # return rotated_matrix

    # Inline
    for i in range(rows//2):
        for j in range(i, rows-i-1):
            temp = m[i][j]
            m[i][j] = m[rows-1-j][i]
            m[rows-1-j][i] = m[rows-1-i][rows-1-j]
            m[rows-1-i][rows-1-j] = m[j][rows-1-i]
            m[j][rows-1-i] = temp
    return m