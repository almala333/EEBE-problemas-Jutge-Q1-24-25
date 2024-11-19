def compra(llista, diners):
    '''
    Paràmetres
    ----------
    llista: List
        Llista de preus dels articles que es volen comprar.
    diners: int
        Quantitat de diners disponibles per fer les compres.

    Retorna
    -------
    int
        El nombre d'articles que es poden comprar amb la quantitat de diners disponibles, 
        tenint en compte que només es poden comprar articles amb un preu entre 10 i la quantitat de diners.

    Tests públics (podeu posar els del Jutge)
    -------------
    >>> compra([100, 125], 55)
    0
    >>> compra([50, 50, 30, 20, 40], 125)
    3
    >>> compra([200, 15, 15] + 100*[20], 30)
    2
    >>> compra([50, 10, 10, 10, 10, 10, 10, 80], 60)
    2
    
    Tests privats
    -------------
    >>> compra([10, 20, 30], 50)
    2
    >>> compra([15, 25, 35, 45], 100)
    3
    >>> compra([5, 15, 25, 35], 40)
    2
    >>> compra([10, 10, 10, 10, 10], 25)
    2
    >>> compra([], 100)
    0
    '''
    
    count = 0  
    for price in llista:
        if price >= 10 and price <= diners:  
            diners -= price 
            count += 1  
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)