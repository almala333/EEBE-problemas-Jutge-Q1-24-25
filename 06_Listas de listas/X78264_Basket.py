def mvp(team):
    '''
    Parametres
    ----------
    team: list
        Llista de jugadors amb la seva nacionalitat i els punts que han fet cada partit
    Retorna
    -------
    tuple:
        Una tuple conformada per una llista mb els noms dels mvps i els punts que han fet
    
    Tests públics 
    -------------
    >>> jug = [  ["Navarro", "Spain", 15, 10, 5],\
                ["Fernandez", "Spain", 10, 5, 5, 2],\
                ["Tomic", "Croatia", 5, 10, 15],\
                ["Birgander", "Sweeden", 7, 10, 2],\
                ["Cook", "USA", 15] ]
    >>> mvp(jug)
    (['Navarro', 'Tomic'], 30)

    Tests privats
    -------------
    >>> mvp([['Messi', 'Argentina', 2, 3, 1], ['Ronaldo', 'Portugal', 1, 2, 0]])
    (['Messi'], 6)

    >>> mvp([['Messi', 'Argentina', 2, 3, 1], ['Ronaldo', 'Portugal', 1, 2, 0], ['Neymar', 'Brasil', 2, 2, 2]])
    (['Messi', 'Neymar'], 6)

    >>> mvp([['Player1', 'Country1', 1, 1, 1], ['Player2', 'Country2', 2, 2, 2]])
    (['Player2'], 6)

    >>> mvp([['Player1', 'Country1', 3, 3, 3], ['Player2', 'Country2', 3, 3, 3]])
    (['Player1', 'Player2'], 9)

    >>> mvp([]) 
    ([], 0)
    
    '''
    best_score = 0
    mvp_list = []
    for i in team:
        if sum(i[2:]) > best_score:
            mvp_list = []
            mvp_list.append(i[0])
            best_score = sum(i[2:])
        elif sum(i[2:]) == best_score:
            mvp_list.append(i[0])
    return (mvp_list, best_score)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
        