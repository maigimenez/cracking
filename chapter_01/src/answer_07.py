def rotate_matrix(m):
    for i in range(len(m)//2):
        for j in range(i, len(m)-i-1):
            aux = m[i][j]
            m[i][j] = m[len(m)-j-1][i]
            m[len(m)-j-1][i] = m[len(m)-i-1][len(m)-j-1]
            m[len(m)-i-1][len(m)-j-1] = m[j][len(m)-i-1]
            m[j][len(m)-i-1] = aux
    return m
