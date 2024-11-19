def is_n_guai(f, n):
    '''
    Parametres
    ----------
    f: List
        Una llista d'enters que es vol analitzar.
    n: int
        Un enter que s'utilitza per determinar la condició de divisibilitat.

    Retorna
    -------
    bool
        Retorna True si cada element de la llista en les posicions múltiples de n és divisible per n, 
        i False en cas contrari.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> is_n_guai([0,1,2,3,4,5,10,10,10,10,25,11],5)
    True
    >>> is_n_guai([0,1,2,3,4,8],5)
    False
    >>> is_n_guai([2,2,4,8,10,12],2)
    True

    Tests privats
    -------------
    >>> is_n_guai([0, 2, 4, 6, 8], 2)
    True
    >>> is_n_guai([1, 2, 3, 4, 5], 3)
    False
    >>> is_n_guai([0, 3, 6, 9, 12], 3)
    True
    >>> is_n_guai([10, 20, 30, 40, 50], 10)
    True
    >>> is_n_guai([1, 2, 3, 4, 5, 6], 1)
    True
    >>> is_n_guai([5, 10, 15, 20, 25], 6)
    False
    '''

    for i in range(len(f)):
        if i % n == 0:
            if f[i] % n != 0:
                return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)