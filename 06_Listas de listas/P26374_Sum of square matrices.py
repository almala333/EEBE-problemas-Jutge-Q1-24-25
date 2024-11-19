def sum(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    '''
    Parametres
    ----------
    a : list
        Matriu de nombres enters, on cada subllista representa una fila de la matriu.
        Precondicions: la matriu ha de ser rectangular (totes les subllistes han de tenir la mateixa longitud).
    b : list
        Matriu de nombres enters, on cada subllista representa una fila de la matriu.
        Precondicions: la matriu ha de ser rectangular (totes les subllistes han de tenir la mateixa longitud) i ha de tenir les mateixes dimensions que 'a'.

    Retorna
    -------
    list
        Una nova matriu que és la suma element a element de les dues matrius 'a' i 'b'.
    
    Tests públics
    -------------
    >>> sum([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[6, 8], [10, 12]]
    
    Tests privats
    -------------
    >>> sum([[0, 0], [0, 0]], [[1, 1], [1, 1]])
    [[1, 1], [1, 1]]
    >>> sum([[1]], [[2]])
    [[3]]
    '''
    
    result = [[0] * len(a) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            result[i][j] = a[i][j] + b[i][j]
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)