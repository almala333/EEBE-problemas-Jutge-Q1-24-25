def int_x2(a, b, n):
    '''
    Paràmetres
    ----------
    a: float
        Extrem inferior de l'interval d'integració.
    b: float
        Extrem superior de l'interval d'integració.
    n: int
        Nombre de subintervals en què es divideix l'interval d'integració.

    Retorna
    -------
    float
        Valor aproximat de la integral de x^2 entre a i b.

    Tests públics
    -------------
    >>> int_x2(1, 4, 1)
    3.0
    >>> int_x2(1, 4, 2)
    10.88
    >>> int_x2(1, 4, 10)
    18.79
    >>> int_x2(1, 4, 50)
    20.55
    >>> int_x2(1, 4, 100)
    20.78
    >>> int_x2(1, 4, 1000)
    20.98
    >>> int_x2(1, 4, 10000)
    21.0

    Tests privats
    -------------
    >>> int_x2(0, 2, 5)
    1.92
    >>> int_x2(-1, 1, 10)
    0.68
    >>> int_x2(2, 6, 20)
    66.16
    >>> int_x2(-2, 2, 50)
    5.34
    
    '''
    baserect = (b-a)/n
    areatot = 0
    for i in range(n):
        areatot += baserect*(a + i*baserect)*(a + i*baserect)
    return round(areatot, 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)