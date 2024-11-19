def persecucion(m1, m2, dini):    
    '''
    Parametres
    ----------
    m1 : str
        Cadena de caràcters que representa el moviment de l'objecte 1.
    m2 : str
        Cadena de caràcters que representa el moviment de l'objecte 2.
    dini : int
        Distància inicial entre els dos objectes.

    Retorna
    -------
    int : El nombre de passos que triguen els objectes a trobar-se, o -1 si no es troben mai.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> persecucion('++=+++++', '+++==+==++', 1)
    5
    >>> persecucion('++=++++++==', '+++==+==+', 17)
    -1


    Tests privats
    -------------
    >>> persecucion('++++', '++++', 0)
    1
    >>> persecucion('++++', '====', 2)
    2
    >>> persecucion('====', '++++', 10)
    -1
    >>> persecucion('+++++++', '+', 5)
    6
    '''
    pos1 = 0
    pos2 = dini
    for i in range(min(len(m1), len(m2))):
        if m1[i] == '+':
            pos1 += 1
        if m2[i] == '+':
            pos2 += 1
        if pos1 >= pos2:
            return i + 1  
    if len(m1) > len(m2):
        for i in range(len(m2), len(m1)):
            if m1[i] == '+':
                pos1 += 1
            if pos1 >= pos2:
                return i + 1  
    elif len(m2) > len(m1):
        for i in range(len(m1), len(m2)):
            if m2[i] == '+':
                pos2 += 1
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)