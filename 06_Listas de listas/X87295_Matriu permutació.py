def matriu_permutacio(mat):
    '''
    Parametres
    ----------
    mat: List
        Matriu que representa una permutació. Ha de ser una matriu quadrada on cada fila i cada columna conté exactament un element igual a 1 i la resta 0.

    Retorna
    -------
    bool
        Retorna True si la matriu és una matriu de permutació, és a dir, si cada fila i cada columna conté exactament un 1 i la resta 0. Retorna False en cas contrari.
    
    Tests públics
    -------------
    >>> matriu_permutacio([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    True
    >>> matriu_permutacio([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    True
    >>> matriu_permutacio([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
    False
    >>> matriu_permutacio([[0, 1], [1, 0]])
    True

    Tests privats
    -------------
    >>> matriu_permutacio([[1, 0], [0, 1]])
    True
    >>> matriu_permutacio([[1, 1], [0, 0]])
    False
    >>> matriu_permutacio([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    False
    >>> matriu_permutacio([[1]])
    True
    >>> matriu_permutacio([[0, 1], [1, 1]])
    False
    '''
    for row in mat:
        if len(row) != len(mat):
            return False
    for i in range(len(mat)):
        if sum(mat[i]) != 1:  
            return False
        column_sum = 0
        for j in range(len(mat)):
            column_sum += mat[j][i]
        if column_sum != 1:
            return False
    
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)