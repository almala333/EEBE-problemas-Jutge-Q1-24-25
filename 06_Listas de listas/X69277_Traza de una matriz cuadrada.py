def traza(mat):
    '''
    Parametres
    ----------
    mat: list
        Matriu quadrada de la que fqarem la suma de la diagonal
        
    Retorna
    -------
    int:
        Suma de la diagonal principal
    
    Tests públics 
    -------------
    >>> traza([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    6
    >>> traza([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    10
    
    Tests privats
    -------------
    >>> traza([[5]])
    5
    >>> traza([[0, 0], [0, 0]])
    0
    >>> traza([[-1, 2], [3, -4]])
    -5
    >>> traza([[1.5, 2.5], [3.5, 4.5]])
    6.0
    '''
    amount = 0
    for i in range(len(mat)):
        amount += mat[i][i]
    return amount

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)