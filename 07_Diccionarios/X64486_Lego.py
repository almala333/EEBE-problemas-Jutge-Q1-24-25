def comptar_peces(d_caixa, d_model):
    '''
    Parametres
    ----------
    d_caixa: dict
        Un diccionari que representa les peces disponibles per color, on la clau és el color i el valor és la quantitat disponible.
    d_model: dict
        Un diccionari que representa les peces requerides per color, on la clau és el color i el valor és la quantitat necessària.

    Retorna
    -------
    dict
        Un diccionari que conté els colors de les peces que falten i la quantitat que falta per a cada color.

    Tests públics
    -------------
    >>> d_caixa = {'vermella':20, 'blava':15, 'groga':25, 'verda': 10, 'negra':10}
    >>> d_model = {'gris': 9, 'vermella':10, 'blava':20, 'groga':6, 'taronja': 3}
    >>> d_falta = {'blava':5, 'gris': 9, 'taronja': 3}
    >>> d_falta == comptar_peces(d_caixa,d_model)
    True

    Tests privats
    -------------
    >>> d_caixa = {'vermella':5, 'blava':10}
    >>> d_model = {'vermella':10, 'blava':15, 'groga':5}
    >>> d_falta = {'vermella':5, 'blava':5, 'groga':5}
    >>> d_falta == comptar_peces(d_caixa, d_model)
    True

    >>> d_caixa = {'vermella':0, 'blava':0}
    >>> d_model = {'vermella':5, 'blava':5, 'groga':5}
    >>> d_falta = {'vermella':5, 'blava':5, 'groga':5}
    >>> d_falta == comptar_peces(d_caixa, d_model)
    True

    >>> d_caixa = {'groga':10}
    >>> d_model = {'groga':5, 'blava':3}
    >>> d_falta = {'blava':3}
    >>> d_falta == comptar_peces(d_caixa, d_model)
    True
    '''

    missing_pieces = {}
    for color in d_model:
        required_quantity = d_model[color]  
        if color in d_caixa:
            available_quantity = d_caixa[color]
        else:
            available_quantity = 0
        if required_quantity > available_quantity:
            missing_pieces[color] = required_quantity - available_quantity
    return missing_pieces

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)