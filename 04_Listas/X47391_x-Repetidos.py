def x_repes(f, n):
    '''
    Parametres
    ----------
    f: List
        Llista d'elements on es volen buscar els elements repetits.
    n: int
        Nombre mínim d'elements repetits que s'han de retornar.

    Retorna
    -------
    List:
        Llista dels primers n elements que es repeteixen a la llista f.
        Si hi ha menys de n elements repetits, retorna una llista buida.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> x_repes([4, 2, 5, 4, 5, 2, 3, 1], 2)
    [4, 2]
    >>> x_repes([4, 2, 5, 4, 5, 2, 3, 1], 4)
    []
    >>> x_repes([4, 2, 5, 4, 5, 2, 3, 1], 3)
    [4, 2, 5]
    >>> x_repes([1, 1, 1, 1, 1, 1], 3)
    []
    >>> x_repes(['good','bye','hello','good','bye'], 2)
    ['good', 'bye']
    
    Tests privats
    -------------
    >>> x_repes([1, 2, 3, 1, 2, 4, 5], 2)
    [1, 2]
    >>> x_repes(['a', 'b', 'a', 'c', 'b', 'd'], 1)
    ['a']
    >>> x_repes([10, 20, 30, 10, 20, 30], 3)
    [10, 20, 30]
    >>> x_repes([], 1)
    []
    >>> x_repes(['x', 'y', 'x', 'y', 'z'], 4)
    []
    '''
    repeated = []
    for i in range(len(f)):
        if f[i] in f[i+1:len(f)]:
            repeated.append(f[i])
        resultado = []
    
    for elemento in repeated:
        if elemento not in resultado:
            resultado.append(elemento)
    

    if len(resultado) < n:
        return []
    
    return resultado[:n]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)