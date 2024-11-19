def elimina_petits(v, m):
    '''
    Parametres
    ----------
    v: List
        Una llista que conté nombres reals.
    m: int
        Un nombre que serveix com a llindar per eliminar els nombres petits.

    Retorna
    -------
    List
        Retorna una nova llista que conté només els nombres de la llista original que són majors que m.
    
    Tests públics
    -------------
    >>> elimina_petits([3, 2, 0.1, 0.08, 0.003], 0.1)
    [3, 2]
    >>> elimina_petits([0.3, 0.2, 0.1], 0.3)
    []
    >>> elimina_petits([], 1)
    []
    >>> elimina_petits([5, 4, 3], 2)
    [5, 4, 3]
    
    Tests privats
    -------------
    >>> elimina_petits([4, 3, 2, 1], 2)
    [4, 3]
    >>> elimina_petits([10, 5, 2, 1], 5)
    [10]
    >>> elimina_petits([-1, -2, -3], 0)
    []
    >>> elimina_petits([0, 0, 0], 0)
    []
    
    '''

    i = 0
    big_num = []
    while i < len(v) and v[i] > m:
        big_num.append(v[i])
        i += 1
    return big_num

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)