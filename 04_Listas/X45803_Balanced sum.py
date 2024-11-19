def suma_equilibrada(f):
    '''
    Parametres
    ----------
    f: list
        List containing all the caracters

    Retorna
    -------
    int 
        Primer index i que compleix que la suma de tots els valors previs es igual a la suma dels valors posteriors
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> suma_equilibrada([1, 1, 1, 1])
    1
    >>> suma_equilibrada([10, 10, 7, 3, 30])
    3
    >>> suma_equilibrada([10, 20])
    -1
    >>> suma_equilibrada([-3, 5, -2])
    2
    >>> suma_equilibrada([0])
    0
    >>> suma_equilibrada([])
    -1
    
    Tests privats
    -------------
    >>> suma_equilibrada([-3, 11, -8])
    2
    >>> suma_equilibrada([0, 0])
    0
    >>> suma_equilibrada([3])
    -1
    
    
    '''
    lowerindex = -1
    leftsum = 0
    totalsum = sum(f)
    rightsum = 0
    for i in range(len(f)):
        leftsum += f[i]
        rightsum =  totalsum - leftsum 
        if leftsum == rightsum:
            lowerindex = i
            return lowerindex
    return  lowerindex


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
