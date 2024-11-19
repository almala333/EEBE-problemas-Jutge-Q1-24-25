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

    '''
    seguretat = 0
    upper = False
    lower = False
    digit = False
    special_character = False
    numbers = '0123456789'
    if len(password) >= 10:
        seguretat  += 1
    for i in password:
        if not upper and 'A'<=i<='Z':
            upper = True
            seguretat += 1
        elif not lower and 'a'<=i<'z':
            lower = True
            seguretat += 1
        elif not digit and i in numbers:
            digit = True
            seguretat += 1
        elif not special_character and i in "$+_*-.,=%":
            special_character = True
            seguretat +=1
        if seguretat == 5:
            return seguretat
    return seguretat


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)