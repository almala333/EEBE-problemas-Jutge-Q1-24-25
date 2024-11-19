def creaDiccionari(l):
    '''
    Parametres
    ----------
    l: list
        Una llista de parells, on cada parell conté un nom (str) i un número de telèfon (str).

    Retorna
    -------
    dict
        Un diccionari on les claus són noms i els valors són els números de telèfon associats a cada nom.
    
    Tests públics
    -------------
    >>> l2 = [["maria", "931111111"], ["pep", "912222222"], ["anna", "93919391"], ["pep", "66477333"], ["maria", "665322888"]]
    >>> d2 = creaDiccionariRepetits(l2)
    >>> d2 == {"maria": ["931111111", "665322888"], "anna": ["93919391"], "pep": ["912222222", "66477333"]}
    True

    Tests privats
    -------------
    >>> creaDiccionari([["josep", "123456789"], ["josep", "987654321"]])
    {'josep': '987654321'}
    >>> creaDiccionari([["laura", "555555555"]])
    {'laura': '555555555'}
    >>> creaDiccionari([["carles", "111111111"], ["marta", "222222222"], ["carles", "333333333"]])
    {'carles': '333333333', 'marta': '222222222'}
    '''

    dictionari = {}
    for nom, telefon in l:
        dictionari[nom] = telefon
    return dictionari

def creaDiccionariRepetits(l):
    '''
    Parametres
    ----------
    l: list
        Una llista de parells, on cada parell conté un nom (str) i un número de telèfon (str).

    Retorna
    -------
    dict
        Un diccionari on les claus són noms i els valors són llistes de números de telèfon associats a cada nom.
    
    Tests públics
    -------------
    >>> l2 = [["maria", "931111111"], ["pep", "912222222"], ["anna", "93919391"], ["pep", "66477333"], ["maria", "665322888"]]
    >>> d2 = creaDiccionariRepetits(l2)
    >>> d2 == {"maria": ["931111111", "665322888"], "anna": ["93919391"], "pep": ["912222222", "66477333"]}
    True

    Tests privats
    -------------
    >>> creaDiccionariRepetits([["josep", "123456789"], ["josep", "987654321"]])
    {'josep': ['123456789', '987654321']}
    >>> creaDiccionariRepetits([["laura", "555555555"]])
    {'laura': ['555555555']}
    >>> creaDiccionariRepetits([["carles", "111111111"], ["marta", "222222222"], ["carles", "333333333"]])
    {'carles': ['111111111', '333333333'], 'marta': ['222222222']}
    '''

    dictionari = {}
    for nom, number in l:
        if nom not in dictionari:
            dictionari[nom] = []
        dictionari[nom].append(number)
    return dictionari

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)