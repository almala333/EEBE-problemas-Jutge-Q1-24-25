def min_Max(M):
    '''
    Parametres
    ----------
    M: List
        Matriu de nombres on cada subllista representa una fila.

    Retorna
    -------
    List
        llista de llistes on cada subllista conté el mínim i el màxim de cada fila 
        i el màxim de cada columna respectivament.
    
    Tests públics
    -------------
    >>> min_Max([[1,2,3],[3,1,2],[2,3,1]])
    [[1, 3], [1, 3], [1, 3]]
    >>> min_Max([[100]])
    [[100, 100]]
    >>> min_Max([[2,2],[2,2]])
    [[2, 2], [2, 2]]
    >>> min_Max([[17, 4],[1,1]])
    [[4, 17], [1, 4]]
    >>> min_Max([[5, 1, 2, 1, -2],[1,21,-1,-2,8],[2,3,1,6,6],[1,2,3,4,5]])
    [[-2, 5], [-2, 21], [1, 3], [1, 6]]

    Tests privats
    -------------
    >>> min_Max([[0, 0], [0, 0]])
    [[0, 0], [0, 0]]
    >>> min_Max([[1]])
    [[1, 1]]
    >>> min_Max([[10, 20, 30], [5, 15, 25]])
    [[10, 10], [5, 20]]
    >>> min_Max([[3, 3, 3], [3, 3, 3]])
    [[3, 3], [3, 3]]
    >>> min_Max([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    [[7, 9], [4, 8], [1, 7]]

    '''
    solution = []
    for i in range(len(M)):
        solution.append([min(M[i]), max(M[j][i] for j in range(len(M)))])
    return solution

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)