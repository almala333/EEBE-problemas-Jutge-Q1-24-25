def frequencies(d):
    '''
    Parametres
    ----------
    d: llista
        Llista de nombres enters o elements per comptar les seves freqüències.

    Retorna
    -------
    dict
        Diccionari amb els elements de la llista original com a claus 
        i les seves freqüències com a valors, ordenat de manera ascendent per les claus.
    
    Tests públics
    -------------
    >>> d = frequencies([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
    >>> d == {1: 5, 2: 6, 3: 4, 4: 2}
    True

    Tests privats
    -------------
    >>> frequencies([])
    {}
    >>> frequencies(['a', 'b', 'a', 'c', 'b', 'a'])
    {'a': 3, 'b': 2, 'c': 1}
    >>> frequencies([5, 5, 5, 5])
    {5: 4}
    
    '''

    fr = {}
    for i in d:
        if i in fr:
            fr[i] += 1
        else:
            fr[i] = 1
    return dict(sorted(fr.items()))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
