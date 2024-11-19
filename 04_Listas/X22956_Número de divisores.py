

def divisores(k):
    '''
    k es un entero mayor que cero
    >>> sorted(divisores(12))
    [1, 2, 3, 4, 6, 12]
    '''
    lista_div = [1]
    if k != 1:
        lista_div.append(k)
    i = 2
    while i*i < k:
        if k % i == 0:
            lista_div.append(i)
            lista_div.append(k//i)
        i += 1
    if k == i*i:
        lista_div.append(i)
    return lista_div

def pos_muchos_divisores(n, listanum):
    '''
    Parametres
    ----------
    n: int
        Un enter que representa el nombre de divisors que busquem.
    listanum: list
        Una llista d'enters on es buscarà el primer nombre que tingui exactament n divisors.

    Retorna
    -------
    int
        Retorna l'índex del primer nombre a la llista que té exactament n divisors. Si no es troba cap nombre, retorna -1.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> pos_muchos_divisores(6, [6, 3, 4, 3, 14, 12 ,15, 14])
    5
    >>> pos_muchos_divisores(1, [13, 15, 13, 15, 13 ,15])
    -1
    >>> pos_muchos_divisores(2, [3, 2, 1])
    0
    >>> pos_muchos_divisores(1, [3, 2, 1])
    2
    >>> pos_muchos_divisores(0, [1])
    -1

    Tests privats
    -------------
    >>> pos_muchos_divisores(3, [6, 8, 10, 12])
    -1
    >>> pos_muchos_divisores(4, [5, 9, 15, 28])
    2
    >>> pos_muchos_divisores(5, [30, 12, 18, 24])
    -1
    >>> pos_muchos_divisores(3, [1, 2, 3])
    -1
    >>> pos_muchos_divisores(2, [4, 6, 8, 10])
    -1
    '''
    for i in range(len(listanum)):
        num = listanum[i]
        if len(divisores(num)) == n:
            return i
    return -1
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)