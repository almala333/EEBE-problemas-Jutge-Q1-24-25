def update_arrival(h, m, d):
    '''
    Paràmetres
    ----------
    h: int
        Les hores.
    m: int
        Els minuts.
    d: int
        Els minuts a afegir.

    Retorna
    -------
    hores, minuts
        Les hores i minuts actualitzats.

    Tests públics 
    -------------
    >>> update_arrival(10, 45, 20)
    (11, 5)
    >>> update_arrival(12, 30, 60)
    (13, 30)
    >>> update_arrival(22, 0, 120)
    (0, 0)
    >>> update_arrival(23, 57, 5 + 24*60)
    (0, 2)
     
    Tests privats
    -------------
    >>> update_arrival(12, 30, 30)
    (13, 0)
    >>> update_arrival(23, 59, 1)
    (0, 0)
    >>> update_arrival(10, 45, 15)
    (11, 0)
    >>> update_arrival(20, 30, 45)
    (21, 15)
    >>> update_arrival(0, 0, 60)
    (1, 0)
    '''

    m = m + d
    h = h + m // 60
    return h % 24, m % 60

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)