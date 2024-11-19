def ca_molar(n, v_ini):
    '''
    Parametres
    ----------
    n: float
        Nombre de mols de solut. Ha de ser un valor positiu.
    v_ini: float
        Volum inicial en litres. Ha de ser un valor positiu.

    Retorna
    -------
    Llista de concentracions en mols per litre (M) calculades per a volums que van des de v_ini fins a 5.0 litres, 
    amb dues decimals de precisió. Si el volum inicial és superior a 5.0, retorna una llista buida.
    
    Tests públics
    -------------
    >>> ca_molar(1,4.75)
    [0.21, 0.2]
    >>> ca_molar(2,5.5)
    []
    >>> ca_molar(2,3.5)
    [0.57, 0.53, 0.5, 0.47, 0.44, 0.42, 0.4]
    >>> ca_molar(1,5)
    [0.2]
    >>> ca_molar(4.76, 4.76)
    [1.0]

    Tests privats
    -------------

    >>> ca_molar(3, 2)
    [1.5, 1.33, 1.2, 1.09, 1.0, 0.92, 0.86, 0.8, 0.75, 0.71, 0.67, 0.63, 0.6]
    >>> ca_molar(5, 5)
    [1.0]
    >>> ca_molar(10, 1)
    [10.0, 8.0, 6.67, 5.71, 5.0, 4.44, 4.0, 3.64, 3.33, 3.08, 2.86, 2.67, 2.5, 2.35, 2.22, 2.11, 2.0]
    
    '''

    concentracions = []
    vmax = 5.0
    v = v_ini

    while v <= vmax:
        c = n / v
        concentracions.append(round(c, 2))
        v += 0.25
    
    return [c for c in concentracions if v_ini <= vmax]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)