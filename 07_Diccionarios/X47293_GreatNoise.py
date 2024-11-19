def calcula_duracion(lista_reproduccion):
    '''
    Parametres
    ----------
    lista_reproduccion: list
        Llista de cançons, on cada cançó és una llista que conté el títol, l'autor, l'àlbum i la durada en segons.

    Retorna
    -------
    tuple
        Una tupla que conté el total de minuts i segons de la durada total de les cançons.

    Tests públics
    -------------
    >>> lista = [["Higher", "Creed", "Greatest Hits", 316],
    ...          ["Basket Case", "Green Day", "Dookie", 182],
    ...          ["Glycerine", "Bush", "Sixteen Stone", 266],
    ...          ["Congregation", "Foo Fighters", "Sonic Highways", 312],
    ...          ["Blackbird", "Alter Bridge", "Blackbird", 478],
    ...          ["Basket Case", "Green Day", "God's FB", 182],
    ...          ["Fuck You", "Bad Religion", "True North", 134],
    ...          ["Higher", "Creed", "Human Clay", 316]]
    >>> calcula_duracion(lista)
    (36, 26)

    Tests privats
    -------------
    >>> lista_test = [["Song1", "Artist1", "Album1", 240],
    ...               ["Song2", "Artist2", "Album2", 180],
    ...               ["Song3", "Artist3", "Album3", 300]]
    >>> calcula_duracion(lista_test)
    (12, 0)
    
    >>> lista_buit = []
    >>> calcula_duracion(lista_buit)
    (0, 0)
    
    >>> lista_una_canco = [["Solo", "Artist", "Album", 150]]
    >>> calcula_duracion(lista_una_canco)
    (2, 30)
    '''
    total_seconds = sum(song[3] for song in lista_reproduccion)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return (minutes, seconds)


def clasificar_duracion(lista_reproduccion):
    '''
    Parametres
    ----------
    lista_reproduccion: list
        Llista de cançons, on cada cançó és una llista que conté el títol, l'autor, l'àlbum i la durada en segons.

    Retorna
    -------
    dict
        Un diccionari que classifica les cançons en tres categories segons la seva durada:
        'a' per a cançons de menys de 3 minuts,
        'b' per a cançons entre 3 i 5 minuts,
        'c' per a cançons de més de 5 minuts.

    Tests públics
    -------------
    >>> lista = [["Higher", "Creed", "Greatest Hits", 316],
    ...          ["Basket Case", "Green Day", "Dookie", 182],
    ...          ["Glycerine", "Bush", "Sixteen Stone", 266],
    ...          ["Congregation", "Foo Fighters", "Sonic Highways", 312],
    ...          ["Blackbird", "Alter Bridge", "Blackbird", 478],
    ...          ["Basket Case", "Green Day", "God's FB", 182],
    ...          ["Fuck You", "Bad Religion", "True North", 134],
    ...          ["Higher", "Creed", "Human Clay", 316]]
    
    >>> clasificacion = clasificar_duracion(lista)
    >>> clasificacion == {'a': 1, 'b': 3, 'c': 4}
    True
    
    Tests privats
    -------------
    >>> lista_test = [["Cançó Curta", "Artista1", "Àlbum1", 120],
    ...               ["Cançó Mitjana", "Artista2", "Àlbum2", 240],
    ...               ["Cançó Llarga", "Artista3", "Àlbum3", 360]]
    >>> clasificar_duracion(lista_test)
    {'a': 1, 'b': 1, 'c': 1}
    
    >>> lista_buit = []
    >>> clasificar_duracion(lista_buit)
    {'a': 0, 'b': 0, 'c': 0}
    
    >>> lista_una_canco = [["Sol", "Artista", "Àlbum", 150]]
    >>> clasificar_duracion(lista_una_canco)
    {'a': 1, 'b': 0, 'c': 0}
    '''
    

    
    duration_count = {'a': 0, 'b': 0, 'c': 0}
    for song in lista_reproduccion:
        duration = song[3]
        if duration < 180:
            duration_count['a'] += 1
        elif 180 <= duration <= 300:
            duration_count['b'] += 1
        else:
            duration_count['c'] += 1
    return duration_count




def estadisticas(lista_reproduccion):
    '''
    Parametres
    ----------
    lista_reproduccion: list
        Llista de cançons, on cada cançó és una llista que conté el títol, l'autor, l'àlbum i la durada en segons.

    Retorna
    -------
    dict
        Un diccionari que conté els títols de les cançons com a claus i una llista d'autors i àlbums com a valors.

    Tests públics
    -------------
    >>> lista = [["Higher", "Creed", "Greatest Hits", 316],
    ...          ["Basket Case", "Green Day", "Dookie", 182],
    ...          ["Glycerine", "Bush", "Sixteen Stone", 266],
    ...          ["Congregation", "Foo Fighters", "Sonic Highways", 312],
    ...          ["Blackbird", "Alter Bridge", "Blackbird", 478],
    ...          ["Basket Case", "Green Day", "God's FB", 182],
    ...          ["Fuck You", "Bad Religion", "True North", 134],
    ...          ["Higher", "Creed", "Human Clay", 316]]
    >>> canciones = estadisticas(lista)
    >>> canciones == {'Higher': ['Creed', 'Greatest Hits', 'Human Clay'],
    ...               'Basket Case': ['Green Day', 'Dookie', "God's FB"],
    ...               'Glycerine': ['Bush', 'Sixteen Stone'],
    ...               'Congregation': ['Foo Fighters', 'Sonic Highways'],
    ...               'Blackbird': ['Alter Bridge', 'Blackbird'],
    ...               'Fuck You': ['Bad Religion', 'True North']}
    True

    Tests privats
    -------------
    >>> lista_test = [["Song1", "Artist1", "Album1", 240],
    ...               ["Song2", "Artist2", "Album2", 180],
    ...               ["Song1", "Artist1", "Album3", 300]]
    >>> estadisticas(lista_test)
    {'Song1': ['Artist1', 'Album1', 'Album3'], 'Song2': ['Artist2', 'Album2']}
    
    >>> lista_buit = []
    >>> estadisticas(lista_buit)
    {}
    
    >>> lista_una_canco = [["Solo", "Artist", "Album", 150]]
    >>> estadisticas(lista_una_canco)
    {'Solo': ['Artist', 'Album']}
    '''
    
    statistics = {}
    for song in lista_reproduccion:
        title = song[0]
        author = song[1]
        album = song[2]
        
        if title not in statistics:
            statistics[title] = [author]
        statistics[title].append(album)
    return statistics


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)