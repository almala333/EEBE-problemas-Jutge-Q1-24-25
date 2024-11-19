def suma(mat):
    '''
    Parametres
    ----------
    mat: list
        La matriu de la que s'han de suar els valors

    Retorna
    -------
    int:
        Suma de tots els valor de la matriu
    
    Tests públics 
    -------------
    >>> suma([[1, 2, 3], [2, 2, 2], [1, 2, 3]])
    18

    Tests privats
    -------------
    >>> suma([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    45
    >>> suma([[10, 20], [30, 40]])
    100
    >>> suma([[1]])
    1
    >>> suma([[], []])
    0
    >>> suma([])
    0
    
    '''
    amount = 0
    for i in range (len(mat)):
        for n in range(len(mat[i])):
            amount += mat[i][n]
    return amount

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)