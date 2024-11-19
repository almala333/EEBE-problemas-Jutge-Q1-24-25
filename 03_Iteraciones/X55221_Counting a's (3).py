def count_a(s, stop):
    '''
    Paràmetres
    ----------
    s: str
        Cadena de caràcters on es comptarà les 'a'.
    stop: str
        Caràcter que fa que la funció pari de comptar.

    Retorna
    -------
    int
        El nombre d'aparicions de la lletra 'a' fins que es troba el caràcter para_aturar. Si no es troba, retorna -1.

    Tests públics 
    -------------
    >>> compte_a('naturally', 'u')
    1
    >>> compte_a('russian', 't')
    -1
    >>> compte_a('adaptation', 'a')
    0
    >>> compte_a('adaptation', 'n')
    3

    Tests privats
    -------------
    >>> compte_a('algoritme', 'e')
    2
    >>> compte_a('informàtica', 'i')
    2
    >>> compte_a('matemàtiques', 'm')
    2
    
    '''
    compte = 0
    for i in s:
        if i == stop:
             return compte
        elif i ==  'a':
            compte += 1
    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)