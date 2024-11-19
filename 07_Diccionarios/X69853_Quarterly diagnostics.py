def stats_diag(ldiags):
    '''
    Parametres
    ----------
    ldiags: list
        Llista de llistes, on cada subllista conté el nom d'un diagnòstic, el número de setmana (1-12) i el nombre de casos.
        Precondicions: la setmana ha de ser un enter entre 1 i 12, i el nombre de casos ha de ser un enter no negatiu.

    Retorna
    -------
    dict
        Un diccionari on les claus són els noms dels diagnòstics i els valors són llistes amb el nombre de casos per cada setmana (1-12).
    
    Tests públics 
    -------------
    >>> ldiags = [['Conjuntivitis', 8, 17], ['Fractura', 3, 14],
    ...       ['Conjuntivitis', 4, 15], ['Infarto', 11, 18],
    ...       ['Conjuntivitis', 11, 18], ['Fractura', 6, 16],
    ...       ['Conjuntivitis', 2, 18], ['Fractura', 7, 10],
    ...       ['Infarto', 8, 15], ['Neumonía', 4, 38],
    ...       ['Fractura', 12, 6], ['Infarto', 2, 20],
    ...       ['Conjuntivitis', 6, 25], ['Conjuntivitis', 5, 14],
    ...       ['Fractura', 8, 13], ['Infarto', 12, 18], ['Neumonía', 7, 28],
    ...       ['Neumonía', 12, 34], ['Fractura', 2, 13], ['Infarto', 4, 25],
    ...       ['Conjuntivitis', 3, 17], ['Conjuntivitis', 7, 20],
    ...       ['Infarto', 9, 18], ['Conjuntivitis', 10, 19], ['Neumonía', 8, 32],
    ...       ['Fractura', 11, 19], ['Neumonía', 3, 40], ['Infarto', 6, 22],
    ...       ['Fractura', 4, 12], ['Neumonía', 5, 31], ['Conjuntivitis', 9, 17],
    ...       ['Fractura', 9, 10], ['Infarto', 7, 18], ['Neumonía', 11, 40],
    ...       ['Infarto', 1, 17], ['Infarto', 5, 12],
    ...       ['Conjuntivitis', 1, 24], ['Fractura', 1, 2],
    ...       ['Infarto', 10, 18], ['Neumonía', 9, 46], ['Fractura', 10, 17],
    ...       ['Neumonía', 10, 39], ['Neumonía', 2, 35], ['Neumonía', 6, 35],
    ...       ['Conjuntivitis', 12, 9], ['Infarto', 3, 24], ['Neumonía', 1, 20],
    ...       ['Fractura', 5, 12]]
    >>> sd = stats_diag(ldiags)
    >>> if sd != {'Conjuntivitis': [24, 18, 17, 15, 14, 25, 20, 17, 17, 19, 18, 9],
    ...       'Neumonía': [20, 35, 40, 38, 31, 35, 28, 32, 46, 39, 40, 34],
    ...       'Fractura': [2, 13, 14, 12, 12, 16, 10, 13, 10, 17, 19, 6],
    ...       'Infarto': [17, 20, 24, 25, 12, 22, 18, 15, 18, 18, 18, 18]}:
    ...     print(sd)

    Tests privats
    -------------
    >>> stats_diag([['Malaltia A', 1, 5], ['Malaltia A', 1, 3], ['Malaltia B', 2, 4], ['Malaltia A', 2, 2], ['Malaltia B', 3, 1]])
    {'Malaltia A': [8, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Malaltia B': [0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    >>> stats_diag([['Malaltia C', 5, 10], ['Malaltia C', 5, 5], 
    ...       ['Malaltia D', 6, 7], ['Malaltia C', 6, 3]])
    {'Malaltia C': [0, 0, 0, 0, 15, 3, 0, 0, 0, 0, 0, 0], 'Malaltia D': [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0]}
    >>> stats_diag([['Malaltia E', 12, 1], ['Malaltia E', 12, 2], 
    ...       ['Malaltia F', 11, 3], ['Malaltia E', 11, 4]])
    {'Malaltia E': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3], 'Malaltia F': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]}
    '''

    diagnosis_stats = {}
    for i in ldiags:
        diagnosis_name = i[0]  
        week_number = i[1] - 1
        cases = i[2]
        if diagnosis_name not in diagnosis_stats:
            diagnosis_stats[diagnosis_name] = [0] * 12
        diagnosis_stats[diagnosis_name][week_number] += cases

    return diagnosis_stats

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)