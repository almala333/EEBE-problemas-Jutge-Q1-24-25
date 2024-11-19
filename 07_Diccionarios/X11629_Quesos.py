def tipo_quesos(quesos):
    '''
    Paràmetres
    ----------
    quesos: list
        Llista de llistes, on cada subllista conté el nom d'un formatge i el seu tipus.
        Precondicions: la llista no ha d'estar buida i cada subllista ha de tenir exactament dos elements.

    Retorna
    -------
    dict
        Diccionari on les claus són els tipus de formatge i els valors són llistes amb els noms dels formatges corresponents.
    
    Tests públics
    -------------
    >>> q = [['Sbrinz', 'añejo'], ['Cheddar', 'semicurado'],
    ...      ['Gouda', 'semicurado'], ['Idiazábal', 'curado'], ['Picón', 'añejo'],
    ...      ['Tronchón', 'tierno'], ['Cottage', 'fresco'], ['Zamorano', 'viejo'],
    ...      ['Gruyere', 'semicurado'], ['Burgos', 'fresco']]
    >>> tq = tipo_quesos(q)
    >>> tq == {'fresco': ['Cottage', 'Burgos'],
    ...        'tierno': ['Tronchón'],
    ...        'semicurado': ['Cheddar', 'Gouda', 'Gruyere'],
    ...        'curado': ['Idiazábal'],
    ...        'viejo': ['Zamorano'],
    ...        'añejo': ['Sbrinz', 'Picón']}
    True
    >>> q = [['Sbrinz', 'añejo'], ['Cheddar', 'semicurado'],
    ...         ['Gouda', 'semicurado'], ['Idiazábal', 'curado'], ['Picón', 'añejo'],
    ...         ['Tronchón', 'tierno'], ['Cottage', 'fresco'],
    ...         ['Gruyere', 'semicurado'], ['Burgos', 'fresco']]
    >>> tq = tipo_quesos(q)
    >>> tq == {'fresco': ['Cottage', 'Burgos'],
    ...        'tierno': ['Tronchón'],
    ...        'semicurado': ['Cheddar', 'Gouda', 'Gruyere'],
    ...        'curado': ['Idiazábal'],
    ...        'añejo': ['Sbrinz', 'Picón']}
    True

    Tests privats
    -------------
    >>> q = [['Roquefort', 'fresco'], ['Feta', 'fresco']]
    >>> tq = tipo_quesos(q)
    >>> tq == {'fresco': ['Roquefort', 'Feta']}
    True
    >>> q = [['Parmesà', 'curado'], ['Manchego', 'viejo'], ['Brie', 'tierno']]
    >>> tq = tipo_quesos(q)
    >>> tq == {'curado': ['Parmesà'], 'viejo': ['Manchego'], 'tierno': ['Brie']}
    True
    >>> q = [['Mozzarella', 'fresco']]
    >>> tq = tipo_quesos(q)
    >>> tq == {'fresco': ['Mozzarella']}
    True
    >>> q = []
    >>> tq = tipo_quesos(q)
    >>> tq == {}
    True
    '''
    
    types = {
        'fresco': [],
        'tierno': [],
        'semicurado': [],
        'curado': [],
        'viejo': [],
        'añejo': []
    }
    for cheese in quesos:
        nombre, kind = cheese
        if kind in types:
            types[kind].append(nombre)
    types = {k: v for k, v in types.items() if v}
    return types

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)