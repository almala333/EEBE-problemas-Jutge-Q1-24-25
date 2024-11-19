def multiples_interval(m, x, y):
    '''
    Parametres
    ----------
    m: int
        nombre del que hem de buscar els seus multiples
    x: int 
        nombre que delimita per abaix els valors entre els que s'ha de buscar si son multimples de m
    y: int 
        nombre que delimita per adalt els valors entre els que s'ha de buscar si son multimples de m

    Retorna
    -------
    list:
        Llista de multiples de m entre x i y

    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> multiples_interval(2, 2, 10)
    [2, 4, 6, 8, 10]
    >>> multiples_interval(5, -5, 4)
    [-5, 0]
    >>> multiples_interval(7, -15, 10)
    [-14, -7, 0, 7]
    >>> multiples_interval(13, 1, 9)
    []
    
    Tests privats
    -------------
    >>> multiples_interval(11, 2, 10)
    []
    >>> multiples_interval(5, 10, 10)
    [10]
    '''
    new_list= []
    for i in range (x, y+1):
        if i % m == 0:
            new_list += [i]
    return  new_list


    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)