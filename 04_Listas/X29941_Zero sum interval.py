def intervalo_suma_cero(f, i):
    '''
    Parametres
    ----------
    f: List
        Una llista de nombres enter que es vol analitzar.
    i: int
        Un índex que indica el punt d'inici de l'anàlisi a la llista.

    Retorna
    -------
    Int:
        Un enter que representa l'índex del primer element on la suma acumulada és zero.
        Si no s'ha trobat cap suma acumulada zero, retorna -1.
    
    Tests públics 
    -------------
    >>> intervalo_suma_cero([1,2,3,-5,-3,2,8,-8],0)
    5
    >>> intervalo_suma_cero([1,2,3,-5,-3,2,8,-8],1)
    3
    >>> intervalo_suma_cero([1,2,3,-5,-3,2,8,-8],5)
    -1

    Tests privats
    -------------
    >>> intervalo_suma_cero([1, -1, 2, -2], 0)
    1
    >>> intervalo_suma_cero([5, -5, 1, -1, 2], 0)
    1
    >>> intervalo_suma_cero([10, 20, -10, -20], 0)
    3
    >>> intervalo_suma_cero([1, 2, 3, 4], 0)
    -1
    '''
    cumulative_sum = 0
    for j in range(i, len(f)):
        cumulative_sum += f[j] 
        if cumulative_sum == 0:
            return j  
    
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)