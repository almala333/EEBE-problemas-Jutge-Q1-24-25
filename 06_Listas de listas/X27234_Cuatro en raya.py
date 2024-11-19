def huecos_columna(tablero, columna):
    '''
    Parametres
    ----------
    tablero: List
        Representa el tauler de joc, on cada element pot ser 0 (espai buit) o un altre valor (ocupat).
    columna: int
        Indica la columna per la qual es volen comptar els espais buits.

    Retorna
    -------
    int
        El nombre d'espais buits (0) que hi ha a la columna especificada del tauler.
    
    Tests públics
    -------------
    >>> tablero = [[2, 0, 0, 0, 2, 1, 0],
    ...            [2, 2, 0, 0, 1, 1, 0],
    ...            [1, 1, 0, 2, 2, 2, 1],
    ...            [1, 2, 0, 2, 2, 1, 2],
    ...            [2, 1, 0, 1, 2, 2, 1],
    ...            [1, 1, 0, 2, 1, 2, 1]]
    >>> huecos_columna(tablero, 3)
    2

    Tests privats
    -------------
    >>> tablero2 = [[0, 0, 0],
    ...             [1, 1, 1],
    ...             [0, 0, 0],
    ...             [1, 0, 1]]
    >>> huecos_columna(tablero2, 0)
    2
    >>> huecos_columna(tablero2, 1)
    3
    >>> huecos_columna(tablero2, 2)
    2
    >>> tablero3 = [[0, 1, 0],
    ...             [0, 0, 0],
    ...             [1, 1, 1],
    ...             [0, 0, 0]]
    >>> huecos_columna(tablero3, 0)
    3
    >>> huecos_columna(tablero3, 1)
    2
    >>> huecos_columna(tablero3, 2)
    3
    '''
    count = 0
    for i in tablero:
        if i[columna] == 0:
            count += 1
    return count

def huecos(tablero):
    '''
    Parametres
    ----------
    tablero: List
        Representa el tauler de joc, on cada element pot ser 0 (espai buit) o un altre valor (ocupat).

    Retorna
    -------
    List[int]
        Una llista que conté el nombre d'espais buits (0) per cada columna del tauler.
    
    Tests públics
    -------------
    >>> tablero = [[2, 0, 0, 0, 2, 1, 0],
    ...            [2, 2, 0, 0, 1, 1, 0],
    ...            [1, 1, 0, 2, 2, 2, 1],
    ...            [1, 2, 0, 2, 2, 1, 2],
    ...            [2, 1, 0, 1, 2, 2, 1],
    ...            [1, 1, 0, 2, 1, 2, 1]]
    >>> huecos(tablero)
    [0, 1, 6, 2, 0, 0, 2]

    Tests privats
    -------------
    >>> tablero2 = [[0, 0, 0],
    ...             [1, 1, 1],
    ...             [0, 0, 0],
    ...             [1, 0, 1]]
    >>> huecos(tablero2)
    [2, 3, 2]
    >>> tablero3 = [[0, 1, 0],
    ...             [0, 0, 0],
    ...             [1, 1, 1],
    ...             [0, 0, 0]]
    >>> huecos(tablero3)
    [3, 2, 3]
    '''
    return [huecos_columna(tablero, col) for col in range(len(tablero[0]))]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)