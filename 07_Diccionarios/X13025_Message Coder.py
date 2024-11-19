def coder(s):
    '''
    Parametres
    ----------
    s: str
        Una cadena de text que es vol codificar. Precondicions: s no ha de ser buida.

    Retorna
    -------
    dict
        Un diccionari on les claus són els caràcters de la cadena d'entrada i els valors són llistes d'índexs
        que indiquen les posicions de cada caràcter en la cadena.

    Tests públics
    -------------
    >>> d_salida = {'m': [0], 'i': [1, 14, 16], 's': [2, 3], 'a': [4, 18], 't': [5],
    ... 'g': [6], 'e': [7, 9], 'p': [8], 'r': [10, 19], 'c': [11, 17], 'o': [12],
    ... 'd': [13], 'f': [15]}
    >>> if d_salida != coder("missatgepercodificar"): print(d_salida)
    >>> d_salida = {'h': [0, 4, 8], 'o': [1, 5, 9], 'l': [2, 6, 10], 'a': [3, 7, 11]}
    >>> if d_salida != coder("holaholahola"): print(d_salida)
    >>> d_salida = {'k': [0, 1, 2]}
    >>> if d_salida != coder("kkk"): print(d_salida)
    >>> d_salida = {'a': [0, 2, 4, 10, 13, 15, 19], 'x': [1, 6, 9, 16], 's': [3], 'z': [5],
    ... 'i': [7], 'n': [8, 11], 'c': [12, 14], 't': [17], 'l': [18]}
    >>> if d_salida != coder("axasazxinxancacaxtla"): print(d_salida)
    >>> d_salida = {'f': [0], 'e': [1, 18], 'l': [2], 'i': [3, 8], 'z': [4], 'n': [5 ],
    ... 'a': [6, 10], 'v': [7], 'd': [9, 11], 'y': [12], 'p': [13, 17], 'r': [14, 19],
    ... 'o': [15, 20], 's': [16], '2': [21], '0': [22], '1': [23], '8': [24]}
    >>> if d_salida != coder("feliznavidadyprospero2018"): print(d_salida)

    Tests privats
    -------------
    >>> coder("abc")  # Exemple amb tres caràcters diferents
    {'a': [0], 'b': [1], 'c': [2]}
    >>> coder("aabbcc")  # Exemple amb caràcters repetits
    {'a': [0, 1], 'b': [2, 3], 'c': [4, 5]}
    >>> coder("")  # Exemple amb cadena buida
    {}
    >>> coder("123321")  # Exemple amb números
    {'1': [0, 5], '2': [1, 4], '3': [2, 3]}
    >>> coder("!@#!!@#")  # Exemple amb caràcters especials
    {'!': [0, 3, 4], '@': [1, 5], '#': [2, 6]}
    
    '''

    d = {}
    index = 0 
    for char in s:
        if char not in d:
            d[char] = []  
        d[char].append(index)  
        index += 1  
    return d


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)