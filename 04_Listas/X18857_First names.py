def es_nom_de_noi(s):
    return s in ['Albert', 'Antoni', 'Lluis', 'Marc', 
                 'Pere', 'Pol', 'Ramon']
def primers_noms(f, n):
    
    '''
    Parametres
    ----------
    f: str
        Llista de strings que contenen els noms a revisar
    n: int
        Numero de noms que es posaran si es troven

    Retorna
    -------
    list:
        Llista de noms de nois si no arriba fins a n noms de nois afageix un 'i cap mes'
    
    Tests públics 
    -------------
    >>> primers_noms(['Ramon', 'Laia', 'Gina', 'Alba', 'Aina', 'Lluis'], 2)
    ['Ramon', 'Lluis']
    >>> primers_noms(['Ramon', 'Laia', 'Gina', 'Alba', 'Aina', 'Lluis'], 3)
    ['Ramon', 'Lluis', 'i cap mes']
    >>> primers_noms(['Laia', 'Gina', 'Alba', 'Aina'], 2)
    ['i cap mes']
    >>> primers_noms(['Pere'], 0)
    []
    >>> primers_noms([], 5)
    ['i cap mes']
    
    Tests privats
    -------------
    >>> primers_noms(['Marc', 'Pere', 'Pol', 'Ramon'], 4)
    ['Marc', 'Pere', 'Pol', 'Ramon']
    >>> primers_noms(['Albert', 'Antoni', 'Lluis', 'Marc', 'Pere', 'Pol', 'Ramon'], 7)
    ['Albert', 'Antoni', 'Lluis', 'Marc', 'Pere', 'Pol', 'Ramon']
    >>> primers_noms(['Laia', 'Gina', 'Alba', 'Aina'], 10)
    ['i cap mes']
    >>> primers_noms(['Pere', 'Laia', 'Gina', 'Alba', 'Aina'], 1)
    ['Pere']
    >>> primers_noms(['Pere', 'Laia', 'Gina', 'Alba', 'Aina'], 10)
    ['Pere', 'i cap mes']
    
    '''
    
    male_name_list = []
    for i in f:
        if es_nom_de_noi(i):
            male_name_list.append(i)
            if len(male_name_list) == n:
                return male_name_list
    male_name_list.append('i cap mes')
    return male_name_list[:n]
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)