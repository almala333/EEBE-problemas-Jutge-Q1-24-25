def leading_hand(h, m):
    '''
    Parametres
    ----------
    h: int
        Hora en format de 0 a 23.
    m: int
        Minuts en format de 0 a 59.

    Retorna
    -------
    str
        Indica quin és el braç que lidera, si és el braç de les hores, el braç dels minuts o si estan empatats.

    Tests públics 
    -------------
    >>> leading_hand(22, 51)
    'minute hand'
    >>> leading_hand(21, 45)
    'draw'
    >>> leading_hand(6, 28)
    'hour hand'
    >>> leading_hand(4, 20)
    'draw'
    
    Tests privats
    -------------
    >>> leading_hand(12, 30)
    'minute hand'
    >>> leading_hand(3, 15)
    'draw'
    >>> leading_hand(9, 42)
    'hour hand'
    >>> leading_hand(24, 0)
    'error invalid data'
    >>> leading_hand(0, 60)
    'error invalid data'
    '''

    if h > 23 or m > 59:
        return 'error invalid data'
    a=(h%12/12)
    b=(m/60)
    if a>b:
        return 'hour hand'
    elif b>a:
        return 'minute hand'
    else:
        return 'draw'

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
   