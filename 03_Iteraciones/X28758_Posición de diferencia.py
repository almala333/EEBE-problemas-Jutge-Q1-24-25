def pos_dif(r, s):
    '''
    Parametres
    ----------
    r: str
        Cadena de caràcters de referència.
    s: str
        Cadena de caràcters a comparar.

    Retorna
    -------
    int
        La posició de la primera diferència entre les dues cadenes, o -1 si són iguals.

    Tests públics
    -------------
    >>> pos_dif('pero', 'peros')
    4
    >>> pos_dif('alaska', 'alaska')
    -1
    >>> pos_dif('caramba', 'calabaza')
    2
    >>> pos_dif('alas', 'ala')
    3

    Tests privats
    -------------
    >>> pos_dif('', '')
    -1
    >>> pos_dif('a', 'b')
    0
    >>> pos_dif('abc', 'abcd')
    3
    >>> pos_dif('abcd', 'abc')
    3
    '''

    for i in range(min(len(r), len(s))):
        if r[i] != s[i]:
            return i
    if len(r) != len(s):
        return min(len(r), len(s))
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)