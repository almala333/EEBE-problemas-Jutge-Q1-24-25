def es_siete_tres(n):
    '''
    Parametres
    ----------
    n: int
        Nombre a comprobar si es un siete tres 

    Retorna
    -------
    bool
        Si el nombre cumpleix la propietat o no
    
    Tests públics 
    -------------
    >>> es_siete_tres(21)
    True
    >>> es_siete_tres(14)
    False
    >>> es_siete_tres(49)
    True
    >>> es_siete_tres(0)
    False
    >>> es_siete_tres(3)
    True
    
    Tests privats
    -------------
    >>> es_siete_tres(1)
    True
    >>> es_siete_tres(7)
    True
    >>> es_siete_tres(9)
    True
    >>> es_siete_tres(21)
    True
    >>> es_siete_tres(27)
    True
    >>> es_siete_tres(63)
    True
    >>> es_siete_tres(81)
    True
    >>> es_siete_tres(14)
    False
    '''
    if n == 0:
        return False
    while n % 7 == 0:
        n //= 7
    
    while n % 3 == 0:
        n //= 3
    return n == 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
