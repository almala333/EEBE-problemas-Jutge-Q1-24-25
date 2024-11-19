def suma_ajustada(limit, k, maxim):
    '''
    Parametres
    ----------
    limit: int
        El límit superior per la suma dels múltiples.
    k: int
        El nombre del qual es volen obtenir els múltiples.
    maxim: int
        El valor màxim fins al qual es consideren els múltiples.

    Retorna
    -------
    list:
        Llista de múltiples de k que la seva suma no supera el límit especificat.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> suma_ajustada(20, 3, 1000)
    [3, 6, 9]
    >>> suma_ajustada(10, 1, 1000)
    [1, 2, 3]
    >>> suma_ajustada(10, 1, 3)
    [1, 2]
    >>> suma_ajustada(100, 2, 10)
    [2, 4, 6, 8]
    >>> suma_ajustada(5, 4, 4)
    []
    >>> suma_ajustada(5, 5, 50)
    [] 
    
    Tests privats
    -------------
    >>> suma_ajustada(15, 3, 30)
    [3, 6, 9]
    >>> suma_ajustada(25, 5, 50)
    [5, 10, 15]
    >>> suma_ajustada(30, 7, 100)
    [7, 14]
    >>> suma_ajustada(0, 1, 10)
    []
    >>> suma_ajustada(50, 10, 100)
    [10, 20, 30, 40]
    '''
    
    multiples = [i for i in range(k, maxim, k)]
    result = []
    current_sum = 0
    for num in multiples:
        if current_sum + num < limit:
            result.append(num)
            current_sum += num
        else:
            return result  
    return result 

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)