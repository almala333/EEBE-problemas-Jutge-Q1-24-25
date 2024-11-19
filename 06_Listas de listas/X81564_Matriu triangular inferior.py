def triangularInferior(m):
    '''
    Paràmetres
    ----------
    m : List
        Matriu que es vol comprovar si és triangular inferior. 
        La matriu ha de ser quadrada (mateix nombre de files i columnes).

    Retorna
    -------
    bool
        Retorna True si la matriu és triangular inferior, és a dir, 
        si tots els elements per sobre de la diagonal principal són zeros.
    
    Tests públics 
    -------------
    >>> triangularInferior([[1, 0, 0], [1, 2, 0], [1, 2, 3]])
    True

    Tests privats
    -------------
    >>> triangularInferior([[0, 0], [0, 0]])
    True
    >>> triangularInferior([[1, 1], [0, 1]])
    False
    >>> triangularInferior([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    True
    >>> triangularInferior([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    True
    >>> triangularInferior([[1, 2, 0], [1, 2, 3], [0, 0, 0]])
    False
    >>> triangularInferior([[1, 0], [0, 2]])
    True
    >>> triangularInferior([[1]])
    True
    >>> triangularInferior([])
    True
    
    '''
    if m == []:
        return True
    if len(m) != len(m[0]):
        return False
    for i in range(len(m)):
        for j in range(len(m)):
            if i < j:
                if m[i][j] != 0:
                    return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)