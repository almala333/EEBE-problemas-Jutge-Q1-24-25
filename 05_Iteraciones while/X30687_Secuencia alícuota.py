def divisores_propios(n):
    '''
    n >= 1
    Devuelve la lista con los divisores propios de n
    Si n no tiene ningun divisor propio, devuelve la lista vacia
 
    >>> divisores_propios(10)
    [1, 2, 5]
    >>> divisores_propios(6)
    [1, 2, 3]
    >>> divisores_propios(1)
    []
    '''
    if n == 1:
        return []
    result = [1]
    d = 2
    while d*d <= n:
        if n%d == 0:
            result.append(d)
            if n//d != d:
                result.append(n//d)
        d += 1
    return result

def secuencia_alicuota(n, maxim):
    '''
    Parametres
    ----------
    n:int
        Nombre del que farem la suma dels seus multiples
    maxim:int 
        Nombre maximn al que poden arribar les sumes 
    Retorna
    -------
    String amb totes les sumes
    
    Tests públics 
    -------------
    >>> secuencia_alicuota(12, 25)
    [12, 16, 15, 9, 4, 3, 1]
    >>> secuencia_alicuota(6, 10)
    [6, 6]
    >>> secuencia_alicuota(95, 100)
    [95, 25, 6, 6]
    >>> secuencia_alicuota(102,300)
    [102, 114, 126, 186, 198, 270, 450]
    >>> secuencia_alicuota(102, 800)
    [102, 114, 126, 186, 198, 270, 450, 759, 393, 135, 105, 87, 33, 15, 9, 4, 3, 1]
    
    Tests privats
    -------------
    >>> secuencia_alicuota(12, 25)
    [12, 16, 15, 9, 4, 3, 1]
    >>> secuencia_alicuota(6, 10)
    [6, 6]
    >>> secuencia_alicuota(95, 100)
    [95, 25, 6, 6]
    >>> secuencia_alicuota(28, 100)
    [28, 28]
    >>> secuencia_alicuota(220, 300)
    [220, 284, 220]
    >>> secuencia_alicuota(24, 100)
    [24, 36, 55, 17, 1]
    '''
    new_list = [n]
    current_sum = n
    break_loop = False
    while (current_sum != 1  and current_sum <= maxim) and not break_loop:
        
        divisors = divisores_propios(current_sum)
        current_sum = sum(divisors)
        break_loop = current_sum in new_list
        new_list.append(current_sum)
        
        
    return new_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

        