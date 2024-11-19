def cercanias(linea, sentido):
    '''
    Paràmetres
    ----------
    linea: int
        El número de línia de les cercanies (entre 1 i 4).
    sentido: str
        La direcció de les cercanies ('N' per nord o 'S' per sud).

    Retorna
    -------
    int
        El nombre d'estacions de la línia de cercanies en la direcció donada.

    Tests públics 
    -------------
    >>> cercanias(3,'N')
    12
    >>> cercanias(7,'N')
    0
    >>> cercanias(4,'S')
    15
    >>> cercanias(2,'W')
    0

    Tests privats
    -------------
    >>> cercanias(1,'N')
    8
    >>> cercanias(1,'S')
    7
    >>> cercanias(2,'N')
    10
    >>> cercanias(2,'S')
    9
    >>> cercanias(3,'S')
    13
    >>> cercanias(4,'N')
    14
    >>> cercanias(5,'N')
    0
    >>> cercanias(0,'S')
    0
    >>> cercanias(3,'E')
    0
    '''

    if linea < 1 or linea > 4 or sentido not in ['N', 'S']:
        return 0
    elif linea == 1:
        return 8 if sentido == 'N' else 7
    elif linea == 2:
        return 10 if sentido == 'N' else 9
    elif linea == 3:
        return 12 if sentido == 'N' else 13
    elif linea == 4:
        return 14 if sentido == 'N' else 15

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
