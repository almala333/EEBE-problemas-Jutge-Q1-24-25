def dicc(ll):
    '''
    Parametres
    ----------
    ll: list of list
        Una llista de llistes on cada subllista conté una paraula incorrecta seguida dels seus sinònims.

    Retorna
    -------
    dict
        Un diccionari on les claus són les paraules incorrectes i els valors són llistes de sinònims corresponents.
    
    Tests públics
    -------------
    >>> ll = [['bonyut',  'malgirbat', 'irregular'],
    ...       ['sapastre', 'incompetent'],
    ...       ['capsigrany', 'curt', 'inhabil'],
    ...       ['bufanuvols', 'somiador'], 
    ...       ['ximplet', 'beneit', 'bonhome'],
    ...       ['tararot', 'belluguet', 'turbulent', 'esvalotat']]
    >>> dicc(ll)
    {'bonyut': ['malgirbat', 'irregular'], 'sapastre': ['incompetent'], 'capsigrany': ['curt', 'inhabil'], 'bufanuvols': ['somiador'], 'ximplet': ['beneit', 'bonhome'], 'tararot': ['belluguet', 'turbulent', 'esvalotat']}

    Tests privats
    -------------
    >>> dicc([['gros', 'voluminós'], ['petit', 'minúscul']])
    {'gros': ['voluminós'], 'petit': ['minúscul']}
    >>> dicc([['feliç', 'content'], ['trist', 'descontent']])
    {'feliç': ['content'], 'trist': ['descontent']}
    '''
    diccionari = {}
    for subllista in ll:
        paraula_incorrecta = subllista[0]
        sinònims = subllista[1:]
        diccionari[paraula_incorrecta] = sinònims
    return diccionari


def correccio(diccionari, textincorrecte):
    '''
    Parametres
    ----------
    diccionari: dict
        Un diccionari on les claus són paraules incorrectes i els valors són llistes de sinònims.
    textincorrecte: str
        Un text que conté paraules incorrectes que es volen corregir.

    Retorna
    -------
    str
        El text corregit amb les paraules incorrectes substituïdes per sinònims.

    Tests públics
    -------------
    >>> ll = [['bonyut',  'malgirbat', 'irregular'],
    ...       ['sapastre', 'incompetent'],
    ...       ['capsigrany', 'curt', 'inhabil'],
    ...       ['bufanuvols', 'somiador'], 
    ...       ['ximplet', 'beneit', 'bonhome'],
    ...       ['tararot', 'belluguet', 'turbulent', 'esvalotat']]
    >>> ti = 'Un bonyut que era un sapastre va anar a cal capsigrany pero el bufanuvols que era un ximplet va acabar essent un tararot'
    >>> correccio(dicc(ll), ti)
    'Un irregular que era un incompetent va anar a cal curt pero el somiador que era un bonhome va acabar essent un turbulent'

    Tests privats
    -------------
    >>> correccio({'gros': ['voluminós'], 'petit': ['minúscul']}, 'El gros i el petit són diferents')
    'El voluminós i el minúscul són diferents'
    >>> correccio({'feliç': ['content'], 'trist': ['descontent']}, 'Estic feliç i trist')
    'Estic content i descontent'
    '''

    paraules = textincorrecte.split()
    textcorregit = []

    for i, paraula in enumerate(paraules):
        if paraula in diccionari:
            sinònims = diccionari[paraula]
            sinònim_correcte = sinònims[i % len(sinònims)]
            textcorregit.append(sinònim_correcte)
        else:
            textcorregit.append(paraula)
    return ' '.join(textcorregit)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)