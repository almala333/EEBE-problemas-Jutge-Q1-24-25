def intercalado(r, s):
    '''
    Parametres
    ----------
    r: str
        Cadena de caràcters que es vol intercalar.
    s: str
        Cadena de caràcters que es vol intercalar.
    
    Retorna
    -------
    str
        Cadena de caràcters resultant de la intercalació de les dues cadenes d'entrada.
    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> intercalado('mel', 'ube')
    'mueble'
    >>> intercalado('RD', '23#####')
    'R2D3#####'
    >>> intercalado('oso','')
    'oso'
    >>> intercalado('przs', 'eeoo')
    'perezoso'

    Tests privats
    -------------
    >>> intercalado('abc', '123')
    'a1b2c3'
    >>> intercalado('Hola', 'Món')
    'HMoólna'
    >>> intercalado('xyz', '')
    'xyz'
    >>> intercalado('', 'xyz')
    'xyz'
    '''
    resultado = ""
    min_len = min(len(r), len(s))
    for i in range(min_len):
        resultado += r[i] + s[i]
    resultado += r[min_len:] + s[min_len:]
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)