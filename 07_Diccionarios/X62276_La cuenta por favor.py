def la_cuenta(carta, consumicion):
    '''
    Parametres
    ----------
    carta: dict
        Un diccionari que conté els plats disponibles i els seus preus.
    consumicion: dict
        Un diccionari que indica quants plats s'han consumit.

    Retorna
    -------
    float o int
        El total de la factura, que és la suma dels preus dels plats multiplicats pel nombre de plats consumits,
        arrodonit a dos decimals, o 0 com un enter si el total és 0.

    Tests públics
    -------------
    >>> carta = {'arroz a banda': 6.5, 'pollo al horno': 5,
    ...          'conejo a la brasa': 7.5, 'judias verdes': 4.0,
    ...          'paella': 7.5, 'pimientos rellenos': 5.2,
    ...          'gazpacho': 4,'potaje de garbanzos': 4.5,
    ...          'calamares a la romana': 7, 'lubina a la sal': 8,
    ...          'bacalao con patatas': 9, 'espinacas': 4,
    ...          'ensalada de atun': 5}
    >>> consumicion = {'conejo a la brasa': 2, 'paella': 1}
    >>> la_cuenta(carta, consumicion)
    22.5
    >>> consumicion = {'arroz a banda': 1, 'pollo al horno': 2,
    ...                'ensalada de atun': 3, 'calamares a la romana': 2,
    ...                'espinacas': 1}
    >>> la_cuenta(carta, consumicion)
    49.5
    
    Tests privats
    -------------
    >>> carta = {'plat1': 10.0, 'plat2': 15.0, 'plat3': 20.0}
    >>> consumicion = {'plat1': 1, 'plat2': 2}
    >>> la_cuenta(carta, consumicion)
    40.0
    >>> consumicion = {'plat3': 3}
    >>> la_cuenta(carta, consumicion)
    60.0
    >>> consumicion = {'plat1': 0, 'plat2': 0}
    >>> la_cuenta(carta, consumicion)
    0.0
    >>> consumicion = {}
    >>> la_cuenta(carta, consumicion)
    0
    '''
    price = 0
    for i in consumicion:
        price += consumicion[i] * carta[i]
        
    return price

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
