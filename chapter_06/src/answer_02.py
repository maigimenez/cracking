def basketball(p):
    # Returns the game with the best probability
    #  0 -> Equal probability
    #  1 -> Game 1
    #  2 -> Game 2
    prob_g1 = p
    prob_g2 = p**3 + 3*(p*p*(1-p))
    if prob_g1 == prob_g2:
        return 0
    elif prob_g1 > prob_g2:
        return 1
    else:
        return 2
