def vuelve(orden):
    """
    Parameters
    ----------
    ordre : str
        Ordre de moviments del robot (nord, sud, est, oest)
        
    Returns
    -------
    boolean
        Retorna True si y sólo si el robot
        termina en la posición de salida.

    Public examples
    ---------------
    >>> vuelve('nseo')
    True
    >>> vuelve('nen')
    False
    
    Private examples
    ----------------
    >>> vuelve('neos')
    True
    >>> vuelve('nos')
    False
    >>> vuelve('')
    True
    >>> vuelve('nseon')
    False
    >>> vuelve('nnseeeo')
    False
    """
    ntimes = 0
    stimes = 0
    otimes = 0
    etimes = 0
    for i in orden:
        if i == 'n':
            ntimes += 1
        elif i == 's':
            stimes += 1
        elif i == 'e':
            etimes += 1
        elif i == 'o':
            otimes += 1
    if ntimes == stimes and etimes == otimes:
        return True
    else:
        return False



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
