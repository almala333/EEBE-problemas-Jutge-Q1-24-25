def leapyear(y):
    '''
    Paràmetres
    ----------
    y: int
        L'any a comprovar si és de traspàs.

    Retorna
    -------
    bool
        Cert si l'any és de traspàs, Fals en cas contrari.

    Tests públics 
    -------------
    >>> leapyear(1999)
    False
    >>> leapyear(1968)
    True
    >>> leapyear(2000)
    True
    >>> leapyear(1800)
    False

    Tests privats
    -------------
    >>> leapyear(2020)
    True
    >>> leapyear(2019)
    False
    >>> leapyear(1900)
    False
    >>> leapyear(2004)
    True
    >>> leapyear(1992)
    True
    >>> leapyear(1987)
    False
    '''

    if y % 4 != 0 or (y % 100 == 0 and not y % 400 == 0):
        return False
    else:
        return True 

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)