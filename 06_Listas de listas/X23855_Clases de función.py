def clase_funcion(f, X, Y):
    '''
    Paràmetres
    ----------
    f: List
        Una llista de parells (x, y) on x pertany a X i y pertany a Y.
    X: List
        Conjunt d'entrades possibles.
    Y: List
        Conjunt de sortides possibles.

    Retorna
    -------
    str
        Retorna 'biyectiva' si la funció és biyectiva, 'inyectiva' si és inyectiva,
        'sobreyectiva' si és sobreyectiva, o 'no es ni inyectiva ni sobreyectiva'
        si no compleix cap d'aquestes propietats.
    
    Tests públics
    -------------
    >>> X = [1, 2, 3]
    >>> Y = [4, 5, 6]
    >>> f = [[1, 4], [2, 5], [3, 6]]
    >>> clase_funcion(f, X, Y)
    'biyectiva'
    >>> f = [[1, 4], [2, 4], [3, 4]]
    >>> clase_funcion(f, X, Y)
    ''
    >>> Y = [4, 5]
    >>> f = [[1, 4], [2, 5], [3, 5]]
    >>> clase_funcion(f, X, Y)
    'sobreyectiva'
    >>> Y = [4, 5, 6, 7]
    >>> f = [[1, 4], [2, 5], [3, 6]]
    >>> clase_funcion(f, X, Y)
    'inyectiva'
    >>> f = [[1, 4], [2, 4], [3, 4]]
    >>> clase_funcion(f, X, Y)
    ''

    Tests privats
    -------------
    >>> clase_funcion([(1, 'a'), (2, 'b'), (3, 'c')], [1, 2, 3], ['a', 'b', 'c'])
    'biyectiva'
    >>> clase_funcion([(1, 'a'), (2, 'b'), (3, 'b')], [1, 2, 3], ['a', 'b'])
    'sobreyectiva'
    >>> clase_funcion([(1, 'a'), (2, 'b'), (3, 'c')], [1, 2, 3], ['a', 'b', 'c', 'd'])
    'inyectiva'
    >>> clase_funcion([(1, 'a'), (2, 'a'), (3, 'b')], [1, 2, 3], ['a', 'b'])
    'sobreyectiva'
    '''
    images = []
    inyectiva = True
    for pair in f:
        if pair[1] in images:
            inyectiva = False
        else:
            images.append(pair[1])
    sobreyectiva = True
    for y in Y:
        if y not in images:
            sobreyectiva = False
    if inyectiva and sobreyectiva:
        return 'biyectiva'
    elif inyectiva:
        return 'inyectiva'
    elif sobreyectiva:
        return 'sobreyectiva'
    else:
        return ''

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)