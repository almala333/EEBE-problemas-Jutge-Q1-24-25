def vocales_andarinas(w):
    '''
    Parametres
    ----------
    w : str
        Una cadena en minúscules.

    Retorna
    -------
    str
        La cadena amb les vocals rotades.

    Tests públics 
    -------------
    >>> vocales_andarinas("patata")
    'petete'
    >>> vocales_andarinas("aeiou")
    'eioua'
    >>> vocales_andarinas("mi mama me mima")
    'mo meme mi mome'
    
    Tests privats
    -------------
    >>> vocales_andarinas("hello world")
    'hillu wurld'
    >>> vocales_andarinas("bcdfghjklmnpqrstvwxyz")
    'bcdfghjklmnpqrstvwxyz'
    >>> vocales_andarinas("")
    ''
    >>> vocales_andarinas("aaaaaa")
    'eeeeee'
    >>> vocales_andarinas("eioua")
    'iouae'
    '''
    
    new_str = ''
    for i in w:
        if i == 'a':
            new_str += 'e'
        elif i == 'e':
            new_str += 'i'
        elif i == 'i':
            new_str += 'o'
        elif i == 'o':
            new_str += 'u'
        elif i == 'u':
            new_str += 'a'
        else:
            new_str += i
    return new_str

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)