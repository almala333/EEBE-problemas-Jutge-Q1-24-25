def ordena3(a, b, c):
    """
    Parameters
    ----------
    a, b, c: valors qualsevols del mateix tipus

    Returns
    -------
        Retorna els valors de a, b i c ordenats de forma creixent.

    Public examples
    ---------------
    >>> ordena3('c', 'b', 'a')
    ('a', 'b', 'c')
    >>> ordena3(1, 2, 1)
    (1, 1, 2)
    """
    if a <= b <= c:
        return (a, b, c)
    elif a <= c <= b:
        return (a, c, b)
    elif b <= a <= c:
        return (b, a, c)
    elif b <= c <= a:
        return (b, c, a)
    elif c <= a <= b:
        return (c, a, b)
    else:
        return (c, b, a)


def ordena2(a, b):
    """
    Parameters
    ----------
    a, b: valors qualsevols del mateix tipus

    Returns
    -------
        Retorna els valors de a i b ordenats de forma creixent.

    Public examples
    ---------------
    >>> ordena2('d', 'b')
    ('b', 'd')
    >>> ordena2(1, 1)
    (1, 1)
    """
    if a <= b:
        return (a, b)
    else:
        return (b, a)


def ordena3_2a2(a, b, c):
    """
    Parameters
    ----------
    a, b, c: valors qualsevols del mateix tipus

    Returns
    -------
        Retorna els valors de a, b i c ordenats de forma creixent.
        Aquesta funció no pot tenir un if i cal resoldre-la cridant
        a la funció ordena2(a, b).

    Public examples
    ---------------
    >>> ordena3_2a2('c', 'b', 'a')
    ('a', 'b', 'c')
    >>> ordena3_2a2(1, 2, 1)
    (1, 1, 2)
    """
    
    (minab,  maxab) = ordena2(a, b)
    (minabc, maxabc) = ordena2(maxab, c)
    (min, mid) = ordena2(minabc, minab)
    return ordena3(min, mid,  maxabc)

    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)