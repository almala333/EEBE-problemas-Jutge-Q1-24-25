def pos_a(s, k):
    '''
    Paràmetres
    ----------
    cadena: str
        La cadena d'entrada per buscar el caràcter 'a'.
    ocorrencia: int
        La k-èsima ocurrencia del caràcter 'a' a buscar.

    Retorna
    -------
    int
        La posició de la k-èsima 'a' a la cadena, o -1 si no existeix.

    Tests públics 
    -------------
    >>> pos_a('', 1)
    -1
    >>> pos_a('hola', 2)
    -1
    >>> pos_a('ara', 3)
    -1
    >>> pos_a('lalaland', 3)
    5
    >>> pos_a('almendro', 1)
    0

    Tests privats
    -------------
    >>> pos_a('banana', 2)
    3
    >>> pos_a('aardvark', 1)
    0
    >>> pos_a('hello', 1)
    -1
    >>> pos_a('aaaa', 4)
    3
    >>> pos_a('abcabc', 2)
    3
    '''

    count_a = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count_a += 1
            if count_a == k:
                return i
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)