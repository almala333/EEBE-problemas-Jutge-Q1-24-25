def cuenta_letras(s, minimo, maximo, excepto):
    """
    Parameters
    ----------
    s : str
        Cadena de caràcters on es comptaran les lletres.
    minimo : str
        Lletra mínima del rang que es vol comptar.
    maximo : str
        Lletra màxima del rang que es vol comptar.
    excepto : str
        Lletres que es volen excloure del compte.

    Returns
    -------
    int
        Retorna el número de letras de 's' que
        están en el rango definido por
        'minimo' y 'maximo' (ambos incluidos)
        y no es ninguna de las que aparecen en
        'excepto'.

    Public examples
    ---------------    
    >>> cuenta_letras('tarari que te vi','a', 'z', '')
    13
    >>> cuenta_letras('parara papa','g', 'r', 'pt')
    2
    >>> cuenta_letras('parara pepin','a', 'z', 'rst')
    9
    >>> cuenta_letras('hola, bla ... bla, adios', 'a' , 'z', 'aeiou')
    8
    
    Private examples
    ----------------
    >>> cuenta_letras('abcxyz', 'a', 'z', 'abcxyz')
    0
    >>> cuenta_letras('abcxyz', 'a', 'z', '')
    6
    >>> cuenta_letras('123456', 'a', 'z', '')
    0
    >>> cuenta_letras('', 'a', 'z', '')
    0
    >>> cuenta_letras('abcdefg', 'a', 'e', 'ace')
    2
    >>> cuenta_letras('abcdefg', 'a', 'e', '')
    5
    """

    amount = 0
    for i in s:
        if i.isalpha() and i >= minimo  and i <= maximo and i not in excepto:
            amount += 1
    return amount
            
     

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)