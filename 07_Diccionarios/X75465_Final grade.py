def nota_final(d_notes, d_proves):
    '''
    Parametres
    ----------
    d_notes: dict
        Un diccionari que conté les notes obtingudes en diferents proves, on les claus són els noms de les proves i els valors són les notes corresponents.
    d_proves: dict
        Un diccionari que conté els percentatges corresponents a cada prova, on les claus són els noms de les proves i els valors són els percentatges (en forma decimal) que representen el pes de cada prova en la nota final.

    Retorna
    -------
    tuple
        Retorna una tupla que conté la nota final calculada (com a float) i un diccionari amb les proves no presentades, on les claus són els noms de les proves i els valors són 'NP'.

    Tests públics 
    -------------
    >>> d_proves = {'lab1':0.1, 'lab2':0.1, 'lab3':0.15, 'lab4': 0.15, 'prac':0.25,
    ...             'teo1':0.10, 'teo2':0.15}
    >>> d_notes = {'teo1': 8, 'lab1':8.5, 'lab2':7.5, 'prac':6.0, 'lab3': 9.0}
    >>> nota = 5.25
    >>> d_no_presentat = {'lab4': 'NP', 'teo2': 'NP'}
    >>> (n, dnp) = nota_final(d_notes, d_proves)
    >>> if (n, dnp) != (nota, d_no_presentat): print(n, dnp)

    Tests privats
    -------------
    >>> d_proves = {'exam1': 0.2, 'exam2': 0.3, 'exam3': 0.5}
    >>> d_notes = {'exam1': 10, 'exam2': 8}
    >>> nota_final(d_notes, d_proves)
    (4.4, {'exam3': 'NP'})
    
    >>> d_proves = {'exam1': 0.4, 'exam2': 0.6}
    >>> d_notes = {'exam1': 5}
    >>> nota_final(d_notes, d_proves)
    (2.0, {'exam2': 'NP'})
    
    >>> d_proves = {'lab1': 0.1, 'lab2': 0.1}
    >>> d_notes = {}
    >>> nota_final(d_notes, d_proves)
    (0.0, {'lab1': 'NP', 'lab2': 'NP'})
    '''
    final_grade = 0.0
    d_no_presentat = {}
    for exam, perc in d_proves.items():
        if exam in d_notes:
            final_grade += d_notes[exam] * perc
        else:
            d_no_presentat[exam] = 'NP'
    final_grade = round(final_grade, 2)
    return final_grade, d_no_presentat

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)