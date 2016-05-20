def one_away(s1, s2):
    dists = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(s1)):
        dists[i+1][0] = i+1
    for i in range(len(s2)):
        dists[0][i+1] = i+1
    for i in range(len(s1)):
        for j in range(len(s2)):
            dists[i+1][j+1] = min(dists[i+1][j],
                                  dists[i][j],
                                  dists[i][j+1])
            if s1[i] != s2[j]:
                dists[i+1][j+1] += 1
    return dists[-1][-1] < 2
