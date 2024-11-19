def t_descubierto(s):
    '''
    Paràmetres
    ----------
    s : str
        Cadena de caràcters que representen la situació de la gent a la cua.

    Retorna
    -------
    int
        Retorna quant temps ha estat la gent en la cola mojant-se,
        sabent que només les tres primeres poden cobrir-se.

    Exemples públics
    --------------- 
    >>> t_descubierto('++++--+')
    1
    >>> t_descubierto('++++++++++----+')
    12
    >>> t_descubierto('+-++--+++---++--')
    0
    
    Exemples privats
    ----------------
    >>> t_descubierto('+++++++++++++')
    10
    >>> t_descubierto('----------')
    0
    >>> t_descubierto('+-+-+-+--+-+-')
    0
    >>> t_descubierto('+++++++++-------')
    11
    >>> t_descubierto('---+++++++++---')
    5
    '''

    count = 0
    time = 0
    for i in s:
        if i == '+':
            count += 1
        else:
            count -= 1
        if count > 3:
            time += 1
    return time


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)