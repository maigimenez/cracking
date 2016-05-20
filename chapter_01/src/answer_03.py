def urlify(s, length):
    for i in range(len(s)):
        if s[i] == ' ':
            for j in range(len(s)-3, i, -1):
                s[j+2] = s[j]
            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'
    return s
