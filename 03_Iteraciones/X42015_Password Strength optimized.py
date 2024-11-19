def fortaleza_password(password):
    '''
    Parametres
    ----------
    password: str
        La contrasenya a avaluar.

    Retorna
    -------
    int
        La puntuació de seguretat de la contrasenya, que varia entre 0 i 5.

    Tests públics
    -------------
    >>> fortaleza_password('A1b2.cdef0')
    5
    >>> fortaleza_password('hola')
    1
    >>> fortaleza_password('P4SsW=rd')
    4
    >>> fortaleza_password('PaSsW=rdddddddddddddddddddd')
    4

    Tests privats
    -------------
    >>> fortaleza_password('abcde')
    1
    >>> fortaleza_password('ABCDEF')
    1
    >>> fortaleza_password('1234567890')
    2
    >>> fortaleza_password('abcdefg hijklmn')
    2
    >>> fortaleza_password('A1b2.cdef0!')
    5
    '''

    seguretat = 0
    if len(password) >= 10:
        seguretat += 1
    if (any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "$+_*-.,=%" for c in password)):
        seguretat += 4
    else:
        seguretat += sum([
            any(c.isupper() for c in password),
            any(c.islower() for c in password),
            any(c.isdigit() for c in password),
            any(c in "$+_*-.,=%" for c in password)
        ])
    return seguretat

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)