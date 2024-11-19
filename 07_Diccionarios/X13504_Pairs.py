def limpia(preferencias):
    '''
    Parametres
    ----------
    preferencias: dict
        Un diccionari que conté els treballadors sense actualitzar, on les claus són els noms dels treballadors
        i els valors són llistes amb les preferències de cada treballador.

    Retorna
    -------
    dict
        Un diccionari que conté els treballadors amb les seves preferències actualitzades, eliminant
        aquelles preferències que no corresponen a treballadors actuals.

    Tests públics
    -------------
    >>> d1 = {'pep': ['pau', 'marc', 'eva'], 'pau': ['ana', 'lluc']}
    >>> d2 = limpia(d1)
    >>> d2 == {'pep': ['pau'], 'pau': []}
    True

    Tests privats
    -------------
    >>> d3 = {'joan': ['pau', 'marc'], 'marc': ['joan', 'lluc'], 'lluc': ['pep']}
    >>> d4 = limpia(d3)
    >>> d4 == {'joan': ['pau'], 'marc': ['joan'], 'lluc': []}
    False
    
    >>> d5 = {'anna': ['pau', 'marc', 'joan'], 'pau': ['anna']}
    >>> d6 = limpia(d5)
    >>> d6 == {'anna': ['pau'], 'pau': ['anna']}
    True
    
    >>> d7 = {'xavi': ['marc', 'joan'], 'marc': ['xavi', 'pau']}
    >>> d8 = limpia(d7)
    >>> d8 == {'xavi': ['marc'], 'marc': ['xavi']}
    True
    '''
    
    cleaned_preferences = {}
    current_workers = preferencias.keys()
    for worker, prefs in preferencias.items():
        cleaned_preferences[worker] = [pref for pref in prefs if pref in current_workers]
    return cleaned_preferences
    
def empareja(ltrab, preferencias):
    '''
    Parametres
    ----------
    ltrab: list
        Una llista que conté els treballadors disponibles per a l'emparellament.
    preferencias: dict
        Un diccionari que conté les preferències dels treballadors.

    Retorna
    -------
    dict
        Un diccionari que associa cada treballador amb la seva llista de companys emparellats.

    Tests públics
    -------------
    >>> serv = ['sabrenia', 'rowhn', 'storms']
    >>> prefs = {'jennafer-lee': ['storms', 'sabrenia', 'sarma', 'nyera'],
    ...          'niloofar': ['jennafer-lee', 'rowhn', 'aaniah', 'brents'],
    ...          'sabrenia': [],
    ...          'rowhn': [],
    ...          'ishrat': ['aaniah', 'lyndell', 'lavarr', 'sarma', 'sanburn'],
    ...          'nyera': ['maxantia'],
    ...          'maxantia': ['nüket', 'storms', 'jerid', 'lavarr', 'nică'],
    ...          'sanburn': ['niloofar'],
    ...          'sarma': ['jerid', 'nüket', 'rowhn', 'sanburn'],
    ...          'aaniah': ['sabrenia', 'nică', 'niloofar', 'jennafer-lee'],
    ...          'nüket': ['nică', 'maxantia'],
    ...          'nică': ['storms', 'lavarr', 'sarma', 'rowhn'],
    ...          'storms': ['aaniah', 'maxantia', 'lavarr', 'nică']}
    >>> emp = empareja(serv, prefs)
    >>> emp == {'sabrenia': [], 'rowhn': [], 'storms': ['maxantia', 'nică']}
    True

    Tests privats
    -------------
    >>> empareja(['worker1', 'worker2'], {'worker1': ['worker2'], 'worker2': ['worker1']})
    {'worker1': ['worker2'], 'worker2': ['worker1']}
    
    >>> empareja(['worker1', 'worker2', 'worker3'], {'worker1': ['worker2', 'worker3'], 'worker2': ['worker1'], 'worker3': []})
    {'worker1': ['worker2'], 'worker2': ['worker1'], 'worker3': []}
    
    >>> empareja(['a', 'b', 'c'], {'a': ['b'], 'b': ['c'], 'c': ['a']})
    {'a': [], 'b': [], 'c': []}
    
    >>> empareja(['x', 'y'], {'x': ['y'], 'y': ['x', 'z']})
    {'x': ['y'], 'y': ['x']}
    
    >>> empareja([], {'a': ['b'], 'b': ['a']})
    {}
    '''
    cleaned_preferences = limpia(preferencias)
    emparejados = {}
    for worker in ltrab:
        emparejados[worker] = []
        for companion in cleaned_preferences.get(worker, []):
            if worker in cleaned_preferences.get(companion, []):
                emparejados[worker].append(companion)

    return emparejados

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)