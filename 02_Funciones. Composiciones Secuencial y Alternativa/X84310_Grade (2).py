def grade(s):
    '''
    Parametres
    ----------
    s: float
        La nota que sera evaluada

    Returna
    -------
    str
        Un string describint la nota evaluada


    Public Tests
    ------------
    >>> grade(4.99)
    'suspens'
    >>> grade(8)
    'notable'
    >>> grade(6.99)
    'aprovat'
    >>> grade(9.5)
    'excel.lent'
    >>> grade(10)
    'MH'

    Private Tests
    ------------
    >>> grade(3)
    'suspens'
    >>> grade(4.5)
    'suspens'
    >>> grade(7.5)
    'notable'
    >>> grade(8.5)
    'notable'
    >>> grade(0)
    'Nota no valida'
    >>> grade(12)
    'Nota no valida'
    '''

    if s < 0:
        nota = 'Nota no valida'
    elif s < 5:
        nota = 'suspens'
    elif s < 7:
        nota = 'aprovat'
    elif s < 9:
        nota = 'notable'
    elif s < 10:
        nota = 'excel.lent'
    elif s > 10:
        nota = 'Nota no valida'
    else:
        nota = 'MH'
    return nota

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)