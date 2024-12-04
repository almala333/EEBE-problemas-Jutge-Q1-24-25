def finanzas(dhab):
    '''
    Paràmetres
    ----------
    dhab: dict
        Un diccionari on les claus són números d'identificació i els valors són llistes que contenen el nom, la ciutat, l'edat i els ingressos.

    Retorna
    -------
    dict
        Un diccionari on les claus són les ciutats i els valors són la suma total dels ingressos de cada ciutat.
    
    Tests públics
    -------------
    >>> dic = {'33950850R': ['ALFONSO JOSE CATALA  CAJA', 'VIC', 33, 43522],
    ...        '36517855Z': ['HUGO BERROJO  CASITAS', 'MATARO', 33, 54376],
    ...        '37383015U': ['GERARD COLOMER  LAZARO', 'MATARO', 42, 48453],
    ...        '46770197K': ['FRANCESC XAVIER BARBERAN  ZAVALA', 'MANRESA', 27,63931],
    ...        '43436441N': ['MIGUEL BARCELO  ALARCÓN', 'GRANOLLERS', 36, 77932],
    ...        '40446681H': ['JOSE MIGUEL GIL  QUER', 'BARCELONA', 47, 45280],
    ...        '52405618J': ['VERONICA BORRUEL  SANAHUJA', 'MATARO', 37, 62910],
    ...        '33947100B': ['ROBERTO JAVIER CASAJOANA  PIÑOL', 'GRANOLLERS', 37, 58152],
    ...        '38145526G': ['JAIME GARRIGA  DEL RIO', 'VIC', 28, 70356],
    ...        '33946091A': ['LAURA MOLINA  RAMOS', 'BARCELONA', 37, 50724]}
    >>> df = finanzas(dic)
    >>> if df != {'VIC': 113878, 'MANRESA': 63931, 'MATARO': 165739,
    ...           'GRANOLLERS': 136084, 'BARCELONA': 96004}:
    ...     print(df)

    Tests privats
    -------------
    >>> finanzas({'11111111A': ['Persona 1', 'BARCELONA', 30, 1000]})
    {'BARCELONA': 1000}
    
    >>> finanzas({'22222222B': ['Persona 2', 'MATARO', 40, 2000], 
    ...            '33333333C': ['Persona 3', 'MATARO', 25, 1500]})
    {'MATARO': 3500}
    
    >>> finanzas({'44444444D': ['Persona 4', 'VIC', 35, 3000], 
    ...            '55555555E': ['Persona 5', 'VIC', 45, 5000], 
    ...            '66666666F': ['Persona 6', 'MANRESA', 50, 2500]})
    {'VIC': 8000, 'MANRESA': 2500}
    
    >>> finanzas({})
    {}
    
    '''

    income_city = {}
    for inhabid, data in dhab.items():
        ciudad = data[1]
        income = data[3]
        if ciudad not in income_city:
            income_city[ciudad] = 0
        income_city[ciudad] += income
    return income_city


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)