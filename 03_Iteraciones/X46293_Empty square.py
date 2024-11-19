def empty_square(n):
    '''
    Parametres
    ----------
    n: int
        Es la cuantitat de * que te cada costat del cuadrat
        
    Retorna
    -------
    Un cuadrat format pels  caràcters * i espais on els costats estan formats per n *

    Tests públics 
    -------------
    >>> empty_square(3)
    ***
    * *
    ***
    >>> empty_square(5)
    *****
    *   *
    *   *
    *   *
    *****

    Tests privats
    -------------
    >>> empty_square(8)
    ********
    *      *
    *      *
    *      *
    *      *
    *      *
    *      *
    ********
    >>> empty_square(14)
    **************
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    *            *
    **************
    
    '''
    for i in range(n):
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n-2) + '*')
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)