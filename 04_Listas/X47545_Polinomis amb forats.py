def len_forat(p, i):
    '''
    Donada una llista p que representa un polinomi no buit d'enters,
    i una posicio i, 0 <= i <= len(p)-1, retorna la logitud del forat 
    a la posicio i
    >>> len_forat([9, 3, 0, 0, 0, 2, 4], 2)
    3
    >>> len_forat([9, 3, 0, 0, 0, 2, 4], 1)
    0
    '''
    j = i
    while j < len(p) and p[j] == 0:
        j += 1
    return j - i

def cerca_forat(p, n):
    '''
    Parametres
    ----------
    p: list[int]
        Una llista d'enters que representa un polinomi, on els zeros representen forats.
    n: int
        La longitud mínima del forat que es vol cercar.

    Retorna
    -------
    tuple[int, int]
        Retorna un tuple (inici, fi) on:
        - inici és la posició del primer zero que forma un forat de longitud almenys n.
        - fi és la posició final del forat. Si no existeix un forat de longitud n, retorna (-1, -1).
        Si n és 0, retorna (0, -1) per indicar que no es requereix cap forat.

    Tests públics (podeu posar els del Jutge)
    -------------
    >>> cerca_forat([9, 3, 0, 0, 0, 2, 4], 2)
    (2, 4)
    >>> cerca_forat([9, 3, 0, 0, 0, 2, 4], 3)
    (2, 4)
    >>> cerca_forat([9, 3, 0, 0, 0, 2, 4], 4)
    (-1, -1)
    >>> cerca_forat([0, 0, 9, 3, 0, 0, 0, 2, 4], 3)
    (4, 6)
    >>> cerca_forat([1, 1, 1], 0)
    (0, -1)

    Tests privats
    -------------
    >>> cerca_forat([0, 0, 0], 1)
    (0, 2)
    >>> cerca_forat([1, 2, 3], 1)
    (-1, -1)
    >>> cerca_forat([0, 1, 0, 0, 1], 2)
    (2, 3)
    >>> cerca_forat([0, 0, 0, 0], 4)
    (0, 3)
    '''
    for i in range(len(p)):
        if p[i] == 0:  
            length = len_forat(p, i)
            if length >= n:  
                return (i, i + length - 1)  
    if n == 0:
        return (0, -1)  
    return (-1, -1)  

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)