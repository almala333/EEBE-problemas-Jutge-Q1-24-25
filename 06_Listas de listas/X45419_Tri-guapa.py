def tri_guapa(mat, a, b, c):
    '''
    Parametres
    ----------
    mat: List
        Matriu quadrada que conté els elements a comprovar.
    a: not defined
        Element que ha d'aparèixer per sota de la diagonal.
    b: not defined
        Element que ha d'aparèixer a la diagonal.
    c: not defined
        Element que ha d'aparèixer per sobre de la diagonal.

    Retorna
    -------
    bool
        Retorna True si la matriu compleix les condicions especificades,
        i sino False.
    
    Tests públics
    -------------
    >>> mat = [[2, 3, 3, 3], [1, 2, 3, 3], [1, 1, 2, 3], [1, 1, 1, 2]]
    >>> tri_guapa(mat, 1, 2, 3)
    True
    >>> mat = [[2, 3, 3, 3], [1, 2, 3, 1], [1, 1, 2, 3], [1, 1, 1, 2]]
    >>> tri_guapa(mat, 1, 2, 3)
    False
    >>> mat = [['a', 'b', 'b'], ['c', 'a', 'b'], ['c', 'c', 'a']]
    >>> tri_guapa(mat, 'c', 'a', 'b')
    True
    >>> mat = [['a', 'b', 'b'], ['c', 'b', 'b'], ['c', 'c', 'a']]
    >>> tri_guapa(mat, 'c', 'a', 'b')
    False
    >>> mat = []
    >>> tri_guapa(mat, 'c', 'a', 'b')
    True

    Tests privats
    -------------
    >>> mat = [[1, 2], [3, 1]]
    >>> tri_guapa(mat, 3, 1, 2)
    True
    >>> mat = [[1, 1], [1, 1]]
    >>> tri_guapa(mat, 1, 1, 1)
    True
    >>> mat = [[1, 2, 3], [4, 1, 5], [6, 7, 1]]
    >>> tri_guapa(mat, 4, 1, 2)
    False
    >>> mat = [[5]]
    >>> tri_guapa(mat, 5, 5, 5)
    True
    '''

    if mat == []:
        return True
    if len(mat) != len(mat[0]):
        return False
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i < j:
                if mat[i][j] != c:
                    return False
            elif i == j:  
                if mat[i][j] != b:
                    return False
            else: 
                if mat[i][j] != a:
                    return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)