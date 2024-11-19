def quasi_diagonal(mat, k):
    '''
    Parametres
    ----------
    mat: list
        Matriu quadrada que volem avaluar. Precondicions: la matriu ha de ser quadrada.
    k: int
        Nombre màxim de valors no zero que es permeten fora de la diagonal. Precondicions: k ha de ser un enter no negatiu.

    Retorna
    -------
    bool
        Retorna True si el nombre de valors no zero fora de la diagonal és menor o igual a k, i False en cas contrari.
    
    Tests públics
    -------------
    >>> quasi_diagonal ([[1, 3, 3], [0, 5, 0], [0, 0, 6]], 2)
    True
    >>> quasi_diagonal ([[1, 3, 0], [0, 5, 0], [0, 0, 6]], 0)
    False

    Tests privats
    -------------
    >>> quasi_diagonal([[1, 0, 0], [0, 2, 0], [0, 0, 3]], 0)
    True
    >>> quasi_diagonal([[1, 2, 0], [0, 0, 0], [0, 0, 0]], 1)
    True
    >>> quasi_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4)
    False
    >>> quasi_diagonal([[0, 0], [0, 0]], 1)
    True
    >>> quasi_diagonal([[1, 1], [1, 1]], 1)
    False
    '''
    count_non_zero = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i != j and mat[i][j] != 0:
                count_non_zero += 1
    return count_non_zero <= k

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)