def fraccion_continua_racional(n, m):
    '''
    Parametres
    ----------
    n: int
        Numerador del numero racional.
    m: int
        Denominador del numero racional. 

    Retorna
    -------
    list
        Una llista de enters que representa la fracció continua del numero racional n/m.

    Tests públics 
    -------------
    >>> fraccion_continua_racional(765, 100)
    [7, 1, 1, 1, 6]
    >>> fraccion_continua_racional(98,35)
    [2, 1, 4]
    >>> fraccion_continua_racional(98,34)
    [2, 1, 7, 2]

    Tests privats
    -------------
    >>> fraccion_continua_racional(13, 7)
    [1, 1, 6]
    >>> fraccion_continua_racional(415, 93)
    [4, 2, 6, 7]
    >>> fraccion_continua_racional(1, 1)
    [1]
    >>> fraccion_continua_racional(0, 5)
    [0]
    '''
    
    resultado = []
    r = None
    while m != 0 and r != 0:
        q = n // m
        r = n % m
        resultado.append(q)
        n, m = m, r
    
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)