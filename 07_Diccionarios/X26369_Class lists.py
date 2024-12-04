def listas_clase(matr):
    '''
    Paràmetres
    ----------
    matr: dict
        Un diccionari on les claus són identificadors d'estudiants i els valors són llistes de grups als quals pertanyen.

    Retorna
    -------
    dict
        Un diccionari on les claus són noms de grups i els valors són llistes d'identificadors d'estudiants que pertanyen a cada grup.
    
    Tests públics
    -------------
    >>> matr = {'5555E': ['I21', 'SD32', 'MC10'],
    ...         '2222B': ['I21', 'DCAD11', 'E10'],
    ...         '4444D': ['I21', 'SD32'],
    ...         '1111A': ['I21', 'DCAD11', 'MC10'],
    ...         '3333C': ['I21', 'SD32', 'E10']}
    >>> lc = listas_clase(matr)
    >>> if lc != {'I21':['1111A','2222B','3333C','4444D','5555E'],
    ...           'DCAD11': ['1111A','2222B'],
    ...           'SD32': ['3333C','4444D','5555E'],
    ...           'MC10': ['1111A','5555E'],
    ...           'E10': ['2222B','3333C']}:
    ...     print(lc)

    Tests privats
    -------------
    >>> listas_clase({'1234A': ['G1', 'G2'], '5678B': ['G1']})
    {'G1': ['1234A', '5678B'], 'G2': ['1234A']}
    
    >>> listas_clase({'A1': ['X1', 'Y1'], 'B2': ['Y1', 'Z1']})
    {'X1': ['A1'], 'Y1': ['A1', 'B2'], 'Z1': ['B2']}
    
    >>> listas_clase({'1': ['A'], '2': ['A', 'B'], '3': ['B']})
    {'A': ['1', '2'], 'B': ['2', '3']}
    
    >>> listas_clase({})
    {}
    
    '''

    groups = {}
    for student_id, group_list in matr.items():
        for group in group_list:
            if group not in groups:
                groups[group] = []
            groups[group].append(student_id)
    
    for group in groups:
        groups[group].sort()
    
    return groups

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)