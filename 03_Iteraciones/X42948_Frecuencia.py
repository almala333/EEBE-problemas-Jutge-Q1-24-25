def frecuencia(s1, s2):
    '''
    Paràmetres
    ----------
    s1: str
        Cadena on es buscarà la freqüència de l'altra cadena.
    s2: str
        Cadena que es buscarà dins la primera cadena.
    
    Retorna
    -------
    int
        La freqüència de la cadena s2 dins la cadena s1.
    
    Tests públics 
    -------------
    >>> frecuencia('','a')
    0
    >>> frecuencia('hola','la')
    1
    >>> frecuencia('lalaland','la')
    3
    >>> frecuencia('aaa', 'aa')
    2

    Tests privats
    -------------
    >>> frecuencia('abcabcabc', 'abc')
    3
    >>> frecuencia('mississippi', 'is')
    2
    >>> frecuencia('banana', 'an')
    2
    >>> frecuencia('abcde', 'xyz')
    0
    >>> frecuencia('aaaa', 'a')
    4
    >>> frecuencia('', '')
    0
    '''
    count = 0
    for i in range(len(s1)):
        if s1[i:i+len(s2)] == s2:
            count += 1
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)