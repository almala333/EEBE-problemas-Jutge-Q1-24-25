def extensions(lfich):
    '''
    Parametres
    ----------
    lfich: list
        Una llista de noms de fitxers amb les seves extensions.

    Retorna
    -------
    dict
        Un diccionari on les claus són les extensions dels fitxers i els valors són
        llistes amb els noms dels fitxers (sense extensió) que corresponen a cada extensió.
    
    Tests públics
    -------------
    >>> f = ['carta.txt', 'resum.docx', 'viva_la_vida.mp3', 'podcast1.mp4',
    ...      'perfil.jpeg', 'doc.txt', 'som_foc.mp3', 'a.b.txt']
    >>> d = extensions(f)
    >>> d == {'txt': ['carta', 'doc', 'a.b'],
    ...       'docx': ['resum'],
    ...       'mp3':['viva_la_vida', 'som_foc'],
    ...       'mp4': ['podcast1'], 'jpeg': ['perfil']}
    True

    Tests privats
    -------------
    >>> f = ['imatge.png', 'document.pdf', 'musica.mp3', 'video.avi']
    >>> d = extensions(f)
    >>> d == {'png': ['imatge'], 'pdf': ['document'], 'mp3': ['musica'], 'avi': ['video']}
    True
    
    >>> f = ['foto.jpeg', 'document.doc', 'video.mp4', 'audio.wav', 'text.txt']
    >>> d = extensions(f)
    >>> d == {'jpeg': ['foto'], 'doc': ['document'], 'mp4': ['video'], 'wav': ['audio'], 'txt': ['text']}
    True
    
    >>> f = ['file1.txt', 'file2.txt', 'file3.txt']
    >>> d = extensions(f)
    >>> d == {'txt': ['file1', 'file2', 'file3']}
    True
    '''
    ext_dict = {}
    for filename in lfich:
        last_dot_index = -1
        for i in range(len(filename)):
            if filename[i] == '.':
                last_dot_index = i
        if last_dot_index != -1:
            name = filename[:last_dot_index]
            ext = filename[last_dot_index + 1:]
            if ext in ext_dict:
                ext_dict[ext].append(name)
            else:
                ext_dict[ext] = [name]
    
    return ext_dict

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)