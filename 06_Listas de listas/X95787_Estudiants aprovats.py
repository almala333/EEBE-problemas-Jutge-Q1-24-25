def aprovats(list_notes, n):
    '''
    Parametres
    ----------
    list_notes: list
        Llistes de notes aamb els seus corresponents dnis 

    Retorna
    -------
    List:
        Llista de dnis dels alumnes aprovats
    
    Tests públics 
    -------------
    >>> aprovats([['40970455X', 5, 4, 6], ['896737498N', 7, 7]], 3)
    ['40970455X']
    >>> aprovats([], 1)
    []
    >>> list_notes = [['45211732R', 0.0, 9.0, 8.5],
    ...               ['87231944N', 8.5, 7.0, 2.0, 8.5],
    ...               ['56349823X'], ['35478121T', 5.0, 6.0, 8.5, 4.5]]
    >>> aprovats(list_notes, 4)
    ['87231944N', '35478121T']
    
    Tests privats
    -------------
    >>> aprovats([], 4)
    []
    >>> aprovats([['5634982X']], 2)
    []
    >>> aprovats([['452117032R', 0.0, 9.0, 8.5], ['8723194N', 8.5, 7.0, 2.0, 8.5]], 3)
    ['452117032R', '8723194N']
    >>> aprovats([['3547812T', 5.0, 6.0, 8.5, 4.5]], 4)
    ['3547812T']
    >>> aprovats([['4097045X', 4.9, 4.9, 4.9]], 3)
    []
    >>> aprovats([['4097045X', 5.0, 5.0, 5.0]], 3)
    ['4097045X']
    '''
    aprovats = []
    for i in range(len(list_notes)):
        if (sum(list_notes[i][1:])/n) >= 5:
            aprovats.append(list_notes[i][0])
    return aprovats

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)