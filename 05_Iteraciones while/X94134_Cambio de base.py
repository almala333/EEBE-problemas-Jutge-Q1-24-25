def decimal_a_base(num, base):
    '''
    Parametres
    ----------
    num: int
        El numero a convertir
    base: int
        La base en la que s'ha de convertir

    Retorna
    -------
    str:
        Un string  que representa el numero en la base especificada    
    Tests públics 
    -------------
    >>> decimal_a_base(3, 2)
    '11'
    >>> decimal_a_base(47, 10)
    '47'
    >>> decimal_a_base(2654, 3)
    '10122022'
    >>> decimal_a_base(187, 5)
    '1222'

    Tests privats
    -------------
    >>> decimal_a_base(0, 2)
    '0'
    >>> decimal_a_base(1, 2)
    '1'
    >>> decimal_a_base(10, 2)
    '1010'
    >>> decimal_a_base(100, 10)
    '100'
    >>> decimal_a_base(100, 5)
    '400'
    >>> decimal_a_base(123456, 10)
    '123456'
    
    '''
    if num == 0:
        return '0'
    
    res = ''
    while num > 0:
        res = str(num % base) + res  
        num //= base  
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
