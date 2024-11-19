def aureo(epsilon):
    '''
    Parametres
    ----------
    epsilon: float
        El valor de epsilon que cal tenir en compte.
    r: float 
        Proporcio del calcul anterior
    fi: int 
        Nombre de la proporcio aurea 1
    fi2: int
        Nombre de la proporcio aurea 1

    Retorna
    -------
    tuple:
    (fi,fi2) on fi i fi2 son els nombre auris que copmpleixen l'enunciat
    
    Tests públics 
    -------------
    >>> aureo(1e-5)
    (610, 987)
    >>> aureo(0.1)
    (5, 8)
    
    Tests privats
    -------------
    >>> aureo(1e-1)
    (5, 8)
    >>> aureo(1e-2)
    (13, 21)
    >>> aureo(1e-3)
    (55, 89)
    >>> aureo(1e-4)
    (144, 233)
    >>> aureo(1e-6)
    (1597, 2584)
    '''
    r = 0 
    fi = 1
    fi2 = 1
    while abs((fi2 / fi) - r) >= epsilon:
        r = fi2 / fi
        aux = fi + fi2 
        fi = fi2
        fi2 = aux  
    
    return (int(fi), int(fi2))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
