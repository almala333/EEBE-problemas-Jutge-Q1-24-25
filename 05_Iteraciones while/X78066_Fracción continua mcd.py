def fraccion_continua_mcd(n, m):
    '''
    Paràmetres
    ----------
    n: int
        El primer nombre enter, que representa el numerador.
    m: int
        El segon nombre enter, que representa el denominador.

    Retorna
    -------
    tuple
        Una tupla que conté tres llistes:
        - La primera llista conté els quocients de la fracció contínua.
        - La segona llista conté els numeradors de les fraccions parcials.
        - La tercera llista conté els denominadors de les fraccions parcials.
    
    Tests públics
    -------------
    >>> fraccion_continua_mcd(972, 421)
    ([2, 3, 4, 5, 6], [2, 7, 30, 157, 972], [1, 3, 13, 68, 421])
    >>> fraccion_continua_mcd(98, 35)
    ([2, 1, 28], [2, 3, 98], [1, 1, 35])
    >>> fraccion_continua_mcd(98, 34)
    ([2, 1, 7, 4], [2, 3, 23, 98], [1, 1, 8, 34])

    Tests privats
    -------------
    >>> fraccion_continua_mcd(10, 2)
    ([10], [10], [2])
    >>> fraccion_continua_mcd(15, 5)
    ([15], [15], [5])
    >>> fraccion_continua_mcd(100, 75)
    ([1, 75], [1, 100], [1, 75])
    
    '''
    q = []
    P = [0, 1]
    Q = [1, 0]
    a, b = n, m

    while a % b != 0:
        q.append(a // b)
        a, b = b, a % b
        P.append(q[-1] * P[-1] + P[-2])
        Q.append(q[-1] * Q[-1] + Q[-2])
    q.append(a)
    P.append(n)
    Q.append(m)
    return (q, P[2:], Q[2:])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)