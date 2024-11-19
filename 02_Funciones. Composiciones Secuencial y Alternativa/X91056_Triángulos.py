def triangulo(costat_a, costat_b, costat_c):
    '''
    Paràmetres
    ----------
    costat_a : int
        Longitud del costat a del triangle.
    costat_b : int
        Longitud del costat b del triangle.
    costat_c : int
        Longitud del costat c del triangle.

    Retorna
    -------
    str
        Retorna un string que indica el tipus de triangle (equilàter, isòsceles o escaleno).

    Tests públics
    -------------
    >>> triangulo(2, 3, 4)
    'escaleno'
    >>> triangulo(2, 2, 3)
    'isosceles'
    >>> triangulo(1, 1, 1)
    'equilatero'
    
    Tests  privats
    -------------
    >>> triangulo(5, 5, 5)
    'equilatero'
    >>> triangulo(3, 3, 4)
    'isosceles'
    >>> triangulo(1, 2, 3)
    'escaleno'
    >>> triangulo(6, 6, 6)
    'equilatero'
    >>> triangulo(2, 3, 3)
    'isosceles'
    >>> triangulo(4, 5, 6)
    'escaleno'
    >>> triangulo(7, 7, 7)
    'equilatero'
    >>> triangulo(3, 4, 4)
    'isosceles'

    '''
    if costat_a == costat_b == costat_c:
        return 'equilatero'
    if costat_a == costat_b or costat_b == costat_c or costat_a == costat_c:
        return 'isosceles'
    else:
        return 'escaleno'
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Tests privats
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

