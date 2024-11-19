def moda(children):
    '''
    Parametres
    ----------
    children: dict
        Un diccionari on les claus són noms de nens i els valors són llistes d'idiomes que parlen.
        Precondicions: el diccionari pot estar buit o contenir noms amb llistes d'idiomes.

    Retorna
    -------
    Llista d'idiomes que són parlats pel màxim nombre de nens. Si hi ha un empat, els idiomes es retornen en ordre alfabètic.
    Si no hi ha nens, es retorna una llista buida.
    
    Tests públics
    -------------
    >>> dicc = {'joan': ['angles', 'mandari'],
    ...         'toni': ['frances'],
    ...         'lluisa': ['catala', 'frances'],
    ...         'mireia': ['angles', 'espanyol', 'alemany'] }
    >>> moda(dicc)
    ['angles', 'frances']
    >>> dicc['pere'] = ['angles', 'hindi']
    >>> moda(dicc)
    ['angles']
    >>> dicc = {}
    >>> moda(dicc)
    []

    Tests privats
    -------------
    >>> dicc = {'a': ['idioma1', 'idioma2'], 'b': ['idioma1']}
    >>> moda(dicc)
    ['idioma1']
    >>> dicc = {'x': ['idiomaA'], 'y': ['idiomaB'], 'z': ['idiomaC']}
    >>> moda(dicc)
    ['idiomaA', 'idiomaB', 'idiomaC']
    >>> dicc = {'maria': ['català', 'angles'], 'josep': ['angles', 'francès'], 'laura': ['català', 'francès']}
    >>> moda(dicc)
    ['angles', 'català', 'francès']
    >>> dicc = {'nina': ['espanyol', 'angles'], 'pablo': ['angles', 'espanyol'], 'carla': ['angles']}
    >>> moda(dicc)
    ['angles']
    '''
    idioma_count = {}
    for idiomes in children.values():
        for idioma in idiomes:
            if idioma in idioma_count:
                idioma_count[idioma] += 1
            else:
                idioma_count[idioma] = 1         
    if not idioma_count:
        return []
    max_count = max(idioma_count.values())
    result = [idioma for idioma, count in idioma_count.items() if count == max_count]
    result.sort()
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)