def analisis(data, limite):
    '''
    Paràmetres
    ----------
    data: llista de llistes
        Una llista que conté subllistes d'elements.
    limite: enter
        Un valor límit que s'utilitza per determinar si una subllista és 'OK' o 'KO'.

    Retorna
    -------
    dict
        Un diccionari que conté el nombre d'elements 'OK' i 'KO' en funció del límit especificat.
    
    Tests públics
    -------------
    # Llista buida
    >>> a = analisis([], 3)
    >>> if a != {'OK': 0, 'KO': 0}: print(a)

    # OK simple
    >>> a = analisis([[1, 1]], 2)
    >>> if a != {'OK': 1, 'KO': 0}: print(a)

    # KO simple
    >>> a = analisis([[1, 1]], 1)
    >>> if a != {'OK': 0, 'KO': 1}: print(a)

    # OK Múltiple
    >>> a = analisis([[1, 1], [2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]], 10)
    >>> if a != {'OK': 4, 'KO': 0}: print(a)

    # Mix
    >>> a = analisis([[1, 1], [2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]], 2)
    >>> if a != {'OK': 2, 'KO': 2}: print(a)

    Tests privats
    -------------
    >>> analisis([[1], [2, 2]], 1)
    {'OK': 1, 'KO': 1}

    >>> analisis([[5, 5, 5], [1, 1, 1, 1]], 3)
    {'OK': 1, 'KO': 1}

    >>> analisis([[0], [], [1, 2]], 2)
    {'OK': 3, 'KO': 0}

    >>> analisis([[1, 1, 1], [2, 2], [3]], 3)
    {'OK': 3, 'KO': 0}
    '''
    result = {'OK': 0, 'KO': 0}
    for i in data:
        if len(i) <= limite:
            result['OK'] += 1
        else:
            result['KO'] += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)