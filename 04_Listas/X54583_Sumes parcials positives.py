def sumes_parcials_pos(v):
    '''
    Parametres
    ----------
    v: list
        Una llista d'enters que pot contenir valors positius i negatius.

    Retorna
    -------
    list
        Una llista que conté les sumes parcials positives de la llista d'entrada.
        Si la suma parcial és negativa o zero, no s'inclou en el resultat.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> sumes_parcials_pos([6, 3, -2, -5, 7])
    [6, 9, 7, 2, 9]
    >>> sumes_parcials_pos([0, 3, -4, -5, 7])
    [3, 1]
    >>> sumes_parcials_pos([])
    []
    >>> sumes_parcials_pos([0, -1, -4, -2])
    []
    
    Tests privats
    -------------
    >>> sumes_parcials_pos([1, 2, 3])
    [1, 3, 6]
    >>> sumes_parcials_pos([-1, -1, 1, 1])
    []
    >>> sumes_parcials_pos([-5, 5, 5])
    [5]
    >>> sumes_parcials_pos([10, -20, 15])
    [10, 5]
    ''' 
    sum = 0
    result = []
    for i in v:
        sum += i
        if sum > 0:
            result.append(sum)  
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)