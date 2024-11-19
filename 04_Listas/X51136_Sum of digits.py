def sumadigitos(num):
    return sum([int(i) for i in list(str(num))])

def sum_dig(f, k, n):
    '''
    Parametres
    ----------
    f : list
        Llista de números enters.
    k : int
        Nombre màxim de resultats a retornar.
    n : int
        Límit per a la suma dels dígits.

    Retorna
    -------
    List
        Llista de números amb suma de dígits superior a n, fins a un màxim de k resultats.

    Tests públics 
    -------------

    >>> sum_dig([10, 50, 56, 71, 999, 42, 83, 93, 27, 83, 27], 2, 15)
    []
    >>> sum_dig([44, 401, 43, 0, 1, 0, 68, 22, 58, 88], 5, -3)
    [44, 401, 43, 0, 1]
    >>> sum_dig([3, 0, 3, 1, 2, 5], 3, 2)
    [3, 3, 5]
    >>> sum_dig([3, 4, 5], 3, 3)
    []
    >>> sum_dig([10, 2, 73, 66, 140, 960, 54, 83, 97, 14, 53], 4,  6)
    [73, 66, 960, 54]
    >>> sum_dig([1,2,3], 0, 1)
    []

    Tests privats
    -------------

    >>> sum_dig([11, 22, 33], 2, 5)
    []
    >>> sum_dig([100, 200, 300], 3, 1)
    []
    >>> sum_dig([1, 1, 1], 1, 3)
    []
    >>> sum_dig([9, 9, 9], 2, 18)
    []
    >>> sum_dig([123, 456, 789], 3, 20)
    []
    '''

    result = []
    for num in f:
        if sumadigitos(num) > n:
            result.append(num)
            if len(result) == k: 
                return result  
    return []  


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)