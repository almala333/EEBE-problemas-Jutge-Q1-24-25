def longmax_cadena_rep(f):
    '''
    Parametres
    ----------
    f: List
        Una llista que conté enters, on es vol trobar la longitud màxima d'una cadena consecutiva de números iguals.

    Retorna
    -------
    int
        La longitud màxima d'una cadena consecutiva de números iguals a la llista donada.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> longmax_cadena_rep([3, 1, 1, 1, 0, 0, 0, 0, 1, 0, 2, 2])
    4
    >>> longmax_cadena_rep([3, 1, 5])
    1
    >>> longmax_cadena_rep([3, 3, 3, 3, 3, 3, 3, 3])
    8
    >>> longmax_cadena_rep([1, 0, 1, 0, 0, 1])
    2
    >>> longmax_cadena_rep([])
    0

    Tests privats
    -------------
    >>> longmax_cadena_rep([1, 1, 1, 1])
    4
    >>> longmax_cadena_rep([2, 2, 3, 3, 3, 3, 2])
    4
    >>> longmax_cadena_rep([5, 5, 5, 5, 5, 5, 5])
    7
    >>> longmax_cadena_rep([1, 2, 3, 4])
    1
    >>> longmax_cadena_rep([0, 0, 0, 1, 1, 1, 1, 1])
    5
    
    '''
    if not f:  
        return 0
    max_length = 1  
    current_length = 1  
    for i in range(1, len(f)):
        if f[i] == f[i - 1]:  
            current_length += 1  
        else:
            if current_length > max_length: 
                max_length = current_length  
            current_length = 1  

    if current_length > max_length:  
        max_length = current_length

    return max_length

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)