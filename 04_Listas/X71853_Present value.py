def valor_presente(I, r):
    '''
    Parametres
    ----------
    I : List
        Sèrie de fluxos financers.
    r : int
        Taxa d'interès mensual.

    Retorna
    -------
    El valor present de la sèrie de fluxos financers.

    Tests públics 
    -------------
    >>> round(valor_presente([5000, 5000, 5000, 45000], 5), 2)
    53169.74
    >>> round(valor_presente([100, -50, 35], 7), 2)
    83.84
    >>> valor_presente([], 3)
    0.0
    
    Tests privats
    -------------
    >>> round(valor_presente([100, 200, 300], 5), 2)
    562.59
    >>> round(valor_presente([500, 600, 700], 10), 2)
    1623.97
    >>> valor_presente([1000], 0)
    1000.0
    '''
    value = 0.0
    for i in range(len(I)):
        value += I[i] / ((1 + r/100) ** i)
    return value

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)