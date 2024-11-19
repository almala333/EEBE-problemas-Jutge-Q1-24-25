def moda(d):
    '''
    Parametres
    ----------
    d: List
        Una llista de números enters dels quals es vol calcular la moda. 
        Precondicions: la llista no ha de ser buida.

    Retorna
    -------
    int
        El valor que apareix amb més freqüència a la llista. Si hi ha un empat, retorna el primer valor que apareix amb la màxima freqüència.
    
    Tests públics
    -------------
    >>> moda([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
    2


    Tests privats
    -------------
    >>> moda([10, 20, 10, 30, 20, 20])
    20
    >>> moda([7, 8, 8, 7, 7, 9, 9])
    7
    >>> moda([4, 4, 4, 5, 5, 5, 6, 6])
    4
    >>> moda([5, 5, 5, 1, 1, 2])
    5
    >>> moda([1, 1, 2, 2, 3])
    1
    '''
    fr = {}
    for i in d:
        if i in fr:
            fr[i] += 1
        else:
            fr[i] = 1
    max_freq = 0
    moda_value = None
    for num in fr:
        freq = fr[num]
        if freq > max_freq:
            max_freq = freq
            moda_value = num

    return moda_value


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)