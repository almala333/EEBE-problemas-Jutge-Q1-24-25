def superats(f, limit):
    '''
    Parametres
    ----------
    f: list
        Llista de valors monetaris que representen les despeses.
    limit: float
        L'import límit per considerar una despesa com a superada.

    Retorna
    -------
    float
        La suma total de les dues primeres despeses que superen el límit. Si no hi ha dues despeses superiors al límit, retorna 0.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> superats([149.99, 50.0, 305.0, 81.50, 62.0], 100.0)
    454.99
    >>> superats([49.99, 50.0, 30.0, 81.50, 62.0], 100.0)
    0
    >>> superats([49.99, 50.0, 30.0, 181.50, 62.0], 100.0)
    0
    
    Tests privats
    -------------
    >>> superats([150.0, 200.0, 50.0], 100.0)
    350.0
    >>> superats([100.0, 90.0, 110.0], 100.0)
    0
    >>> superats([200.0, 300.0, 400.0], 250.0)
    700.0
    >>> superats([], 50.0)
    0
    >>> superats([25.0, 30.0, 40.0], 100.0)
    0
    '''
    money_spend_over_amount = 0
    for i in f:
        if i > limit:
            if money_spend_over_amount == 0:
                money_spend_over_amount = i
            else:
                money_spend_over_amount += i
                return money_spend_over_amount
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)