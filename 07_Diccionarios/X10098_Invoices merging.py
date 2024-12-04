def fusion_facturas(fact1, fact2):
    '''
    Paràmetres
    ----------
    fact1: dict
        Un diccionari que associa noms de productes amb els seus preus.
    fact2: dict
        Un diccionari que associa noms de productes amb els seus preus.

    Retorna
    -------
    dict
        Un diccionari que associa noms de productes amb el seu preu acumulat 
        sumant els preus dels dos diccionaris d'entrada.
    
    Tests públics
    -------------
    >>> f1 = {'prod1': 1, 'prod2': 2}
    >>> f2 = {'prod1': 1, 'prod3': 2}
    >>> fus = fusion_facturas(f1, f2)
    >>> if fus != {'prod1': 2, 'prod2': 2, 'prod3': 2}: print(fus)

    Tests privats
    -------------
    >>> fusion_facturas({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    {'a': 1, 'b': 5, 'c': 4}
    
    >>> fusion_facturas({}, {'x': 10})
    {'x': 10}
    
    >>> fusion_facturas({'x': 5}, {})
    {'x': 5}
    
    >>> fusion_facturas({'apple': 1.0}, {'apple': 2.0, 'banana': 1.5})
    {'apple': 3.0, 'banana': 1.5}
    '''

    combined_facts = {}
    for product, price in fact1.items():
        combined_facts[product] = combined_facts.get(product, 0) + price
    for product, price in fact2.items():
        combined_facts[product] = combined_facts.get(product, 0) + price

    return combined_facts

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)