import math
def fraccion_continua_raiz(n):
    '''
    Parametres
    ----------
    n: int
        Un nombre enter positiu del qual volem calcular la fracció contínua de la seva arrel quadrada.

    Retorna
    -------
    list
        Retorna una llista que conté la seqüència de la fracció contínua de l'arrel quadrada de n.
    
    Tests públics 
    -------------
    >>> fraccion_continua_raiz(14)
    [3, 1, 2, 1, 6]
    >>> fraccion_continua_raiz(67)
    [8, 5, 2, 1, 1, 7, 1, 1, 2, 5, 16]
    >>> fraccion_continua_raiz(2)
    [1, 2]

    Tests privats
    -------------
    >>> fraccion_continua_raiz(3)
    [1, 1, 2]
    >>> fraccion_continua_raiz(5)
    [2, 4]
    >>> fraccion_continua_raiz(8)
    [2, 1, 4]
    >>> fraccion_continua_raiz(11)
    [3, 3, 6]
    
    '''

    a0 = int(math.sqrt(n))
    m, d, a = 0, 1, a0
    sequence = []
    seen = []
    
    while (m, d, a) not in seen:
        seen.append((m, d, a))
        sequence.append(a)
        m = d * a - m
        d = (n - m ** 2) // d
        a = (a0 + m) // d
    return sequence

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)