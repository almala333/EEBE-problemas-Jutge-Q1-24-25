def is_perfect_number(n):
    '''
    Paràmetres
    ----------
    n : int
        El nombre a comprovar si és perfecte.
    
    Retorna
    -------
    bool
        True si el nombre és perfecte, sino False.
    
    Tests públics 
    -------------    
    >>> is_perfect_number(6)
    True
    >>> is_perfect_number(8)
    False
    >>> is_perfect_number(28)
    True
    >>> is_perfect_number(496)
    True
    >>> is_perfect_number(1)
    False

    Tests privats
    -------------    
    >>> is_perfect_number(8128)
    True
    >>> is_perfect_number(100)
    False
    >>> is_perfect_number(2)
    False
    
    '''
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    if divisors_sum == n:
        return True
    else:
        return False 

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)