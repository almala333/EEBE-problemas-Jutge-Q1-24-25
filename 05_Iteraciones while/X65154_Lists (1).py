def count_diff(f):
    '''
    Parametres
    ----------
    f: List
        Una llista que conté nombres enters.

    Retorna
    -------
    int
        El nombre de valors únics presents a la llista.
    
    Tests públics 
    -------------
    >>> count_diff([3, -1, 0, 3 ,2, 0])
    4

    Tests privats
    -------------
    >>> count_diff([1, 1, 1, 1])
    1
    >>> count_diff([1, 2, 3, 4])
    4
    >>> count_diff([])
    0
    
    '''    
    unique_values = set()
    i = 0
    while i < len(f):
        unique_values.add(f[i])
        i += 1
    return len(unique_values)

def product(u, v):
    '''
    Parametres
    ----------
    u: List
        Una llista que conté nombres reals.
    v: List
        Una altra llista que conté nombres reals de la mateixa longitud que u.

    Retorna
    -------
    float
        El producte escalar de les dues llistes.
    
    Tests públics 
    -------------
    >>> product([1/3, 0, -1], [3/2, 1/2, 2])
    -1.5
    
    Tests privats
    -------------
    >>> product([1, 2, 3], [4, 5, 6])
    32.0
    >>> product([0, 0], [1, 2])
    0.0
    >>> product([-1, -2], [1, 2])
    -5.0

    '''

    scalar_product = 0.0
    i = 0
    while i < len(u):
        scalar_product += u[i] * v[i]
        i += 1
    return scalar_product

def delete_multiples(k, f):
    '''
    Parametres
    ----------
    k: int
        Un nombre enter que s'utilitzarà per eliminar els múltiples.
    f: List
        Una llista que conté nombres enters.

    Retorna
    -------
    List
        Una nova llista que conté els elements de f que no són múltiples de k.
    
    Tests públics 
    -------------
    >>> delete_multiples(2, [6, 3, -2, -5, 7])
    [3, -5, 7]

    Tests privats
    -------------
    >>> delete_multiples(3, [3, 6, 9, 12])
    []
    >>> delete_multiples(5, [1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> delete_multiples(1, [10, 20, 30])
    []

    '''

    result = []
    i = 0
    while i < len(f):
        if f[i] % k != 0:
            result.append(f[i])
        i += 1
    return result

def erato(n):
    '''
    Parametres
    ----------
    n: int
        Un nombre enter que indica el límit superior per a la generació de nombres primers.

    Retorna
    -------
    List
        Una llista de nombres primers menors que n.
    
    Tests públics 
    -------------
    >>> erato(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    Tests privats
    -------------
    >>> erato(10)
    [2, 3, 5, 7]
    >>> erato(2)
    []
    >>> erato(1)
    []

    '''

    if n <= 2:
        return []
    
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    start = 2
    while start * start < n:
        if sieve[start]:
            multiple = start * start
            while multiple < n:
                sieve[multiple] = False
                multiple += start
        start += 1
    
    primes = []
    i = 0
    while i < n:
        if sieve[i]:
            primes.append(i)
        i += 1
    
    return primes

def merge(f, g):
    '''
    Parametres
    ----------
    f: List
        Una llista que conté nombres enters.
    g: List
        Una altra llista que conté nombres enters.

    Retorna
    -------
    List
        Una llista que conté els elements de f i g ordenats ascendentment.
    
    Tests públics 
    -------------
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]

    Tests privats
    -------------
    >>> merge([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([1, 3, 5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> merge([], [1, 2, 3])
    [1, 2, 3]

    '''

    result = []
    i = j = 0
    while i < len(f) and j < len(g):
        if f[i] < g[j]:
            result.append(f[i])
            i += 1
        else:
            result.append(g[j])
            j += 1
    
    while i < len(f):
        result.append(f[i])
        i += 1
    
    while j < len(g):
        result.append(g[j])
        j += 1
    
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

