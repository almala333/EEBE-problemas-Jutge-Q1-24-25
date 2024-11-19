def habitantes(lista, pob):
    '''
    Parametres
    ----------
    lista: list
        Una llista de tuples on cada tupla conté informació sobre una persona (nom, població, riquesa).
    pob: str
        El nom de la població per la qual es vol filtrar la llista de persones.

    Retorna
    -------
    list
        Una llista de tuples que conté les persones que viuen a la població especificada.

    Tests públics
    -------------
    >>> lista = [['PEDRO','Badalona',37676], ['FELIX','Badalona',42251],
    ...          ['JESUS','Badalona',58760], ['MARIA','Badalona',39378],
    ...          ['JOSE', 'Badalona',53306], ['JUAN', 'Barcelona',50374],
    ...          ['SERGIO', 'Barcelona',37583], ['POL', 'Barcelona',52048],
    ...          ['VICTORIANO', 'Barcelona',35484], ['CARLES', 'Barcelona',40362],
    ...          ['MARTÍ', 'Gerona', 47029], ['JOAN', 'Vic', 57647],
    ...          ['ROSER', 'Gerona', 47873], ['PAULA', 'Gerona', 52538],
    ...          ['ANTONIO','Vic', 55043], ['TERESA', 'Vic', 43762]]
    >>> habitantes(lista,'Gerona')
    [['MARTÍ', 'Gerona', 47029], ['ROSER', 'Gerona', 47873], ['PAULA', 'Gerona', 52538]]

    Tests privats
    -------------
    >>> habitantes([("Anna", "Barcelona", 3000), ("Marc", "Madrid", 2500)], "Barcelona")
    [('Anna', 'Barcelona', 3000)]
    
    >>> habitantes([("Juan Carlos I", "Abu Dhabi", 40000000), ("Trabajador random", "Abu Dhabi", 1000)], "Abu Dhabi")
    [('Juan Carlos I', 'Abu Dhabi', 40000000), ('Trabajador random', 'Abu Dhabi', 1000)]
    
    >>> habitantes([], "Barcelona")
    []
    '''
    list_pob = []
    for i in lista:
        if i[1] == pob:
            list_pob.append(i)
    return list_pob

def ricos(lista, pob):
    '''
    Parametres
    ----------
    lista: list
        Una llista de tuples on cada tupla conté informació sobre una persona (nom, població, riquesa).
    pob: str
        El nom de la població per la qual es vol trobar les persones més riques.

    Retorna
    -------
    list
        Una llista amb les dues persones més riques de la població especificada.

    Tests públics
    -------------
    >>> lista = [['PEDRO','Badalona',37676], ['FELIX','Badalona',42251],
    ...          ['JESUS','Badalona',58760], ['MARIA','Badalona',39378],
    ...          ['JOSE', 'Badalona',53306], ['JUAN', 'Barcelona',50374],
    ...          ['SERGIO', 'Barcelona',37583], ['POL', 'Barcelona',52048],
    ...          ['VICTORIANO', 'Barcelona',35484], ['CARLES', 'Barcelona',40362],
    ...          ['MARTÍ', 'Gerona', 47029], ['JOAN', 'Vic', 57647],
    ...          ['ROSER', 'Gerona', 47873], ['PAULA', 'Gerona', 52538],
    ...          ['ANTONIO','Vic', 55043], ['TERESA', 'Vic', 43762]]

    >>> ricos(lista,'Gerona')
    [['PAULA', 'Gerona', 52538], ['ROSER', 'Gerona', 47873]]
    
    Tests privats
    -------------
    >>> ricos([("Anna", "Barcelona", 3000), ("Marc", "Madrid", 2500)], "Barcelona")
    [('Anna', 'Barcelona', 3000)]

    >>> ricos([("Juan Carlos I", "Abu Dhabi", 40000000), ("Trabajador random", "Abu Dhabi", 1000)], "Abu Dhabi")
    [('Juan Carlos I', 'Abu Dhabi', 40000000), ('Trabajador random', 'Abu Dhabi', 1000)]

    >>> ricos([], "Barcelona")
    []
    '''
    habitants_pob = habitantes(lista, pob)
    if not habitants_pob:
        return []
    if len(habitants_pob) == 1:
        return habitants_pob
    for i in range(len(habitants_pob)):
        for j in range(0, len(habitants_pob) - i - 1):
            if habitants_pob[j][2] < habitants_pob[j + 1][2]: 
                habitants_pob[j], habitants_pob[j + 1] = habitants_pob[j + 1], habitants_pob[j]
    return habitants_pob[:2]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)