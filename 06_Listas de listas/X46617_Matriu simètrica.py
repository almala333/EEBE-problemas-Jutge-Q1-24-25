def simetrica(m):
    '''
    Paràmetres
    ----------
    m: List
        Matriu quadrada que es vol comprovar si és simètrica. Precondicions: 
        la matriu ha de ser una llista de llistes de la mateixa longitud.

    Retorna
    -------
    bool
        Retorna True si la matriu és simètrica, és a dir, si m[i][j] == m[j][i] 
        per a tots els i i j, i False en cas contrari.
    
    Tests públics
    -------------
    >>> simetrica([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    True

    Tests privats
    -------------
    >>> simetrica([[1, 1], [1, 1]])
    True
    >>> simetrica([[1, 2, 3], [2, 1, 4], [3, 4, 1]])
    True
    >>> simetrica([[1, 2], [2, 3]])
    True
    >>> simetrica([[5]])
    True
    >>> simetrica([[1, 2], [3, 4]])
    False
    >>> simetrica([])
    True
    '''
    if m == []:
        return True
    if len(m) != len(m[0]):
        return False
    for i in range(len(m)):
        for j in range(len(m)):
            if i < j:
                if m[i][j] != m[j][i]:
                    return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)