def createQuery(userTerms, terms):
    query = [0] * len(terms)
    for x in userTerms:
        i = 0
        for y in terms:
            if x == y:
                query[i] = 1
            i = i + 1

    return query