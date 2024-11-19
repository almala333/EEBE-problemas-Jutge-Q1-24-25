def intersection(v1, v2):
    
    '''
    Parametres
    ----------
    v1: List
        Una llista d'enters ordenada en ordre creixent.
    v2: List
        Una altra llista d'enters ordenada en ordre creixent.

    Retorna
    -------
    List
        Una llista amb els elements comuns de v1 i v2, ordenada en ordre creixent i sense duplicats.
    
    Tests públics 
    -------------
    >>> intersection([1, 2, 2, 3], [2, 2, 3, 4])
    [2, 3]
    >>> intersection([], [1, 2, 3])
    []
    >>> intersection([1, 2, 3], [])
    []
    >>> intersection([1, 3, 5], [2, 4, 6])
    []
    >>> intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    [3, 4, 5]
    >>> intersection([1, 2, 2, 2, 3], [2, 2, 3, 4])
    [2, 3]
    
    Tests privats
    -------------
    >>> intersection([1, 1, 1], [1, 1, 1])
    [1]
    >>> intersection([5, 6, 7], [6, 7, 8])
    [6, 7]
    >>> intersection([10, 20, 30], [15, 25, 35])
    []
    >>> intersection([1, 2, 3, 4], [1, 2, 2, 3])
    [1, 2, 3]
    >>> intersection([1, 2, 3], [4, 5, 6])
    []
    
    '''
    result = []
    i, j = 0, 0
    
    while i < len(v1) and j < len(v2):
        if v1[i] < v2[j]:
            i += 1
        elif v1[i] > v2[j]:
            j += 1
        else:
            if not result or v1[i] != result[-1]:
                result.append(v1[i])
            i += 1
            j += 1
    
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)