def votsMinim(dic, minim):
    '''
    Parametres
    ----------
    dic: dict
        Un diccionari on les claus són els noms dels candidats i els valors són els vots obtinguts.
    minim: int
        Un enter que representa el nombre mínim de vots.

    Retorna
    -------
    bool
        Retorna True si hi ha algun candidat que no hagi assolit un nombre de vots superior a 'minim'.
        Retorna False en cas contrari.
    
    Tests públics
    -------------
    >>> dvots = {'Joan Pere Jorbina Palau': 570, 'Niceto Brunildo Fornells': 679,
    ...  'Mariona Puig Peix': 701, 'Adriana de Tor Quemada': 451}
    >>> votsMinim(dvots, 400)
    False
    >>> votsMinim(dvots, 600)
    True
    
    Tests privats
    -------------
    >>> votsMinim({'Candidat A': 300}, 250)
    False
    >>> votsMinim({'Candidat B': 100}, 150)
    True
    '''
    for vots in dic.values():
        if vots <= minim:
            return True
    return False

def candidatMesVotat(dic):
    '''
    Parametres
    ----------
    dic: dict
        Un diccionari on les claus són els noms dels candidats i els valors són els vots obtinguts.

    Retorna
    -------
    str
        El nom i cognoms del candidat més votat.
    
    Tests públics
    -------------
    >>> dvots = {'Joan Pere Jorbina Palau': 570, 'Niceto Brunildo Fornells': 679,
    ...  'Mariona Puig Peix': 701, 'Adriana de Tor Quemada': 451}
    >>> candidatMesVotat(dvots)
    'Mariona Puig Peix'
    
    Tests privats
    -------------
    >>> candidatMesVotat({'Candidat A': 100, 'Candidat B': 200})
    'Candidat B'
    >>> candidatMesVotat({'Candidat X': 50})
    'Candidat X'
    '''
    return max(dic, key=dic.get)

def votsIngressos(dvots, ding):
    '''
    Parametres
    ----------
    dvots: dict
        Un diccionari on les claus són els noms dels candidats i els valors són els vots obtinguts.
    ding: dict
        Un diccionari on les claus són els noms de les persones i els valors són els seus ingressos.

    Retorna
    -------
    list
        Una llista dels candidats dels que es desconeix els ingressos, ordenada alfabèticament.
    
    Tests públics
    -------------
    >>> dvots = {'Joan Pere Jorbina Palau': 570, 'Niceto Brunildo Fornells': 679,
    ...  'Mariona Puig Peix': 701, 'Adriana de Tor Quemada': 451}
    >>> ding = {'Mariona Puig Peix': 15456, 'Arnau Osorio Lucas': 27654,
    ...  'Arnau Brigat Pelfred': 18654, 'Niceto Brunildo Fornells': 14567}
    >>> votsIngressos(dvots, ding)
    ['Adriana de Tor Quemada', 'Joan Pere Jorbina Palau']
    
    Tests privats
    -------------
    >>> votsIngressos({'Candidat A': 500}, {'Candidat A': 300, 'Candidat B': 400})
    []
    >>> votsIngressos({'Candidat C': 600, 'Candidat D': 700}, {'Candidat D': 800})
    ['Candidat C']
    '''
    desconeguts = [candidat for candidat in dvots if candidat not in ding]
    return sorted(desconeguts)

def rics(dvots, ding):
    '''
    Parametres
    ----------
    dvots: dict
        Un diccionari on les claus són els noms dels candidats i els valors són els vots obtinguts.
    ding: dict
        Un diccionari on les claus són els noms de les persones i els valors són els seus ingressos.

    Retorna
    -------
    list
        Una llista amb els noms de les tres persones més riques del municipi, amb un asterisc ('*') al costat del nom si és un candidat.
    
    Tests públics
    -------------
    >>> dvots = {'Joan Pere Jorbina Palau': 570, 'Niceto Brunildo Fornells': 679,
    ...  'Mariona Puig Peix': 701, 'Adriana de Tor Quemada': 451}
    >>> ding = {'Mariona Puig Peix': 15456, 'Arnau Osorio Lucas': 27654,
    ...  'Arnau Brigat Pelfred': 18654, 'Niceto Brunildo Fornells': 14567}
    >>> rics(dvots, ding)
    ['Arnau Osorio Lucas', 'Arnau Brigat Pelfred', 'Mariona Puig Peix*']
    
    Tests privats
    -------------
    >>> rics({'Candidat A': 100}, {'Candidat A': 500, 'Candidat B': 600, 'Candidat C': 700})
    ['Candidat C', 'Candidat B', 'Candidat A*']
    >>> rics({'Candidat D': 200, 'Candidat E': 300}, {'Candidat D': 800, 'Candidat E': 900, 'Candidat F': 1000})
    ['Candidat F', 'Candidat E*', 'Candidat D*']
    '''
    ingressos_ordenats = sorted(ding.items(), key=lambda item: item[1], reverse=True)
    
    resultats = []
    for nom, ingressos in ingressos_ordenats[:3]:
        if nom in dvots:
            resultats.append(f"{nom}*")
        else:
            resultats.append(nom)
    
    return resultats


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)