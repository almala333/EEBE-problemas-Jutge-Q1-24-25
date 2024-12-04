def acciones(pers, items):
    '''
    Parametres
    ----------
    pers: dict
        Un diccionari que representa un personatge amb les claus 'nombre', 'clase', 'nivel' i 'mochila'.
    items: dict
        Un diccionari que relaciona els noms dels objectes amb les accions que es poden realitzar amb ells.

    Retorna
    -------
    Llista d'accions que el personatge pot realitzar amb els objectes de la seva motxilla.
    
    Tests públics
    -------------
    >>> pers = {'nombre': 'Juan', 'clase': 'mago', 'nivel': 3, 'mochila': ['cuchillo', 'varita', 'libro', 'ganzúa']}
    >>> items = {'cuchillo': 'cortar', 'ganzúa': 'abrir', 'libro': 'aprender', 'varita': 'conjurar', 'vaso': 'beber', 'linterna': 'iluminar'}
    >>> acciones(pers, items)
    ['cortar', 'conjurar', 'aprender', 'abrir']
    
    Tests privats
    -------------
    >>> acciones({'nombre': 'Maria', 'clase': 'guerrero', 'nivel': 2, 'mochila': ['espada', 'cuchillo']}, {'cuchillo': 'cortar', 'espada': 'atacar'})
    ['atacar', 'cortar']
    >>> acciones({'nombre': 'Luis', 'clase': 'mago', 'nivel': 5, 'mochila': ['varita', 'libro', 'vaso']}, {'varita': 'conjurar', 'libro': 'aprender', 'vaso': 'beber'})
    ['conjurar', 'aprender', 'beber']
    
    '''

    acciones_posibles = []
    for objeto in pers['mochila']:
        if objeto in items:
            acciones_posibles.append(items[objeto])
    return acciones_posibles

def equipables(pers, items):
    '''
    Parametres
    ----------
    pers: dict
        Un diccionari que representa un personatge amb les claus 'nombre', 'clase', 'nivel' i 'mochila'.
    items: dict
        Un diccionari que relaciona els noms dels objectes amb el seu nivell d'equipament.

    Retorna
    -------
    Llista d'objectes que el personatge pot equipar segons el seu nivell.
    
    Tests públics
    -------------
    >>> pers = {'nombre': 'Juan', 'clase': 'mago', 'nivel': 3, 'mochila': ['cuchillo', 'varita', 'libro', 'ganzúa']}
    >>> items = {'cuchillo': 5, 'ganzúa': 1, 'varita': 3, 'vaso': 2, 'libro': 2, 'linterna': 3}
    >>> equipables(pers, items)
    ['varita', 'libro', 'ganzúa']
    
    Tests privats
    -------------
    >>> equipables({'nombre': 'Ana', 'clase': 'guerrero', 'nivel': 4, 'mochila': ['espada', 'cuchillo']}, {'cuchillo': 2, 'espada': 5})
    ['cuchillo']
    >>> equipables({'nombre': 'Pedro', 'clase': 'mago', 'nivel': 1, 'mochila': ['varita', 'libro', 'ganzúa']}, {'varita': 3, 'libro': 1, 'ganzúa': 1})
    ['libro', 'ganzúa']
    
    '''
    objetos_equipables = []
    for objeto in pers['mochila']:
        if objeto in items:
            if items[objeto] <= pers['nivel']:
                objetos_equipables.append(objeto)
    return objetos_equipables

def usables(pers, items):
    '''
    Parametres
    ----------
    pers: dict
        Un diccionari que representa un personatge amb les claus 'nombre', 'clase', 'nivel' i 'mochila'.
    items: dict
        Un diccionari que relaciona els noms dels objectes amb les classes que poden utilitzar-los.

    Retorna
    -------
    Llista d'objectes que el personatge pot utilitzar segons la seva classe.
    
    Tests públics
    -------------
    >>> pers = {'nombre': 'Juan ', 'clase': 'mago', 'nivel': 3, 'mochila': ['cuchillo', 'varita', 'libro', 'ganzúa']}
    >>> items = {'cuchillo': ['ladrón', 'guerrero'], 'varita': ['mago'], 'libro': ['mago'], 'espada': ['guerrero'], 'ganzúa': ['ladrón']}
    >>> usables(pers, items)
    ['varita', 'libro']
    
    Tests privats
    -------------
    >>> usables({'nombre': 'Sofia', 'clase': 'mago', 'nivel': 3, 'mochila': ['varita', 'espada']}, {'varita': ['mago'], 'espada': ['guerrero']})
    ['varita']
    >>> usables({'nombre': 'Carlos', 'clase': 'guerrero', 'nivel': 2, 'mochila': ['cuchillo', 'espada']}, {'cuchillo': ['ladrón', 'guerrero'], 'espada': ['guerrero']})
    ['cuchillo', 'espada']
    
    '''

    objetos_usables = []
    for objeto in pers['mochila']:
        if objeto in items:
            if pers['clase'] in items[objeto]:
                objetos_usables.append(objeto)
    return objetos_usables

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)