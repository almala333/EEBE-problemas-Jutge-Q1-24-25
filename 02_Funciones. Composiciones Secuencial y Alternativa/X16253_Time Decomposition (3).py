def decompose(n):
    '''
    Paràmetres
    ----------
    n: int
        El nombre de segons a descompondre.

    Retorna
    -------
    hores, minuts, segons
        Les hores, minuts i segons descompostos del nombre de segons.

    Tests públics 
    -------------
    >>> decompose(147)
    (0, 2, 27)
    >>> decompose(3661)
    (1, 1, 1)
    >>> decompose(76234)
    (21, 10, 34)

    Tests privats
    -------------
    >>> decompose(9000)
    (2, 30, 0)
    >>> decompose(5400)
    (1, 30, 0)
    >>> decompose(1800)
    (0, 30, 0)
    '''

    return (n//3600, (n%3600)//60, n%60)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)