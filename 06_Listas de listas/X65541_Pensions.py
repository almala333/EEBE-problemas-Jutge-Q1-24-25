def promigDespeses(p):
    '''
    Parametres
    ----------
    p : list
        Llista que conté les dades d'una persona, on el primer element és un codi, 
        el segon és el nom, el tercer és l'edat, i els següents són les despeses.

    Retorna
    -------
    float
        El promig de les despeses de la persona, arrodonit a dues decimals.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> promigDespeses(l[0])
    600.67
    '''
    despeses = p[3:]
    promig = sum(despeses) / len(despeses)
    return round(promig, 2)

def promigEdats(lp):
    '''
    Parametres
    ----------
    lp : list
        Llista que conté subllistes, on cada subllista representa una persona 
        amb el seu codi, nom, edat i opcionalment altres dades.

    Retorna
    -------
    float
        El promig de les edats de les persones en la llista, arrodonit a una decimal.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> promigEdats(l)
    71.0
    '''
    edats = [p[2] for p in lp]
    promig = sum(edats) / len(edats)
    return round(promig, 2)

def edatsExtremes(lp):
    '''
    Parametres
    ----------
    lp: list
        Una llista de llistes, on cada subllista conté informació d'una persona, 
        incloent el seu DNI, nom i edats.

    Retorna
    -------
    tuple
        Una tupla que conté l'edat mínima i l'edat màxima de les persones presents a la llista.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> edatsExtremes(l)
    (68, 75)
    '''
    edats = [p[2] for p in lp]
    return (min(edats), max(edats))

def sumaPromig(lp):
    '''
    Parametres
    ----------
    lp: list
        Una llista de llistes, on cada subllista conté informació d'una persona, 
        incloent el seu DNI, nom, edat i diverses puntuacions.

    Retorna
    -------
    float
        La suma total de les puntuacions de totes les persones dividida pel 
        nombre total de puntuacions, és a dir, la mitjana de les puntuacions.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> sumaPromig (l)
    2370.84
    '''
    suma = sum(promigDespeses(p) for p in lp)
    return round(suma, 2)

def maximPromig(lp):
    '''
    Parametres
    ----------
    lp: list
        Una llista de llistes, on cada subllista conté informació d'una persona, 
        incloent el seu DNI, nom, edat i diverses puntuacions.

    Retorna
    -------
    float
        El màxim de les mitjanes de les despeses de totes les persones, 
        arrodonit a dues decimals.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> maximPromig(l)
    624.0
    '''
    max_promig = max(promigDespeses(p) for p in lp)
    return round(max_promig, 2)

def despesaPromig(lp):
    '''
    Parametres
    ----------
    lp: list
        Una llista de llistes, on cada subllista conté informació d'una persona, 
        incloent el seu DNI, nom, edat i diverses despeses.

    Retorna
    -------
    list
        Una llista de tuples, on cada tuple conté la mitjana de les despeses 
        d'una persona i el seu DNI, ordenada per la mitjana de menor a major.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> despesaPromig(l)
    [532.0, 600.67, 614.17, 624.0]
    '''
    result = []
    for p in lp:
        result.append(promigDespeses(p))
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result

def despesaPromigSuperior(lp, d):
    '''
    Parametres
    ----------
    lp: list
        Una llista de llistes, on cada subllista conté informació d'una persona, 
        incloent el seu DNI, nom, edat i diverses despeses.
    d: float
        Un valor numèric que representa el llindar de despesa mitjana.

    Retorna
    -------
    list
        Una llista que conté el DNI de les persones que tenen una despesa 
        mitjana superior al llindar especificat, juntament amb la seva mitjana 
        de despeses.

    Tests públics
    -------------
    >>> l = [['1111A','Joan',68,640,589,573],
    ...      ['2222D','Pepa',69,710,550,570,698,645,512],
    ...      ['3333J','Anna',72,530,534],
    ...      ['4444N','Pep',75,770,645,630,650,590,481,602]]
    >>> despesaPromigSuperior(l, 600)
    ['1111A', 68]
    '''
    for p in lp:
        if promigDespeses(p) > d:
            return [p[0], p[2]]  
    return []

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)