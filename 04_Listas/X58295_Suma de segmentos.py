def suma_seg(f, n):
    '''
    Paràmetres
    ----------
    f : List
        Una llista de nombres enters que es vol sumar.
    n : int
        Un nombre enter que representa el límit superior per a la suma.

    Retorna
    -------
    (bool, int)
        Retorna una tupla on el primer element indica si la suma acumulada
        ha superat el límit n (True) o no (False), i el segon element és
        l'índex en què s'ha superat el límit, o -1 si no s'ha superat.

    Tests públics 
    -------------
    >>> suma_seg([1, -2, 3, 4, 5, 6], 10)
    (True, 4)
    >>> suma_seg([1, 3, 1, -2, 0, 1], 12)
    (False, -1)
    >>> suma_seg([1, -1], 1)
    (False, -1)
    >>> suma_seg([-1, 1], 0)
    (False, -1)
    >>> suma_seg([1, -1], 0)
    (True, 0)
    >>> suma_seg([3], 2)
    (True, 0)
    >>> suma_seg([], 0)
    (False, -1)

    Tests privats
    -------------
    >>> suma_seg([2, 2, 2], 5)
    (True, 2)
    >>> suma_seg([1, 1, 1, 1], 3)
    (True, 2)
    >>> suma_seg([0, 0, 0], 0)
    (True, 0)
    >>> suma_seg([1, 2, 3], 10)
    (True, 2)
    >>> suma_seg([5, 5, 5], 15)
    (False, -1)
    '''
    sums = 0
    for i in range(len(f)):
        sums += f[i]
        if sums > n:
            return (True, i)
    return (False, -1)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)