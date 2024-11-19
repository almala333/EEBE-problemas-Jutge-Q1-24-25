def next_word_list(w, f):
    '''
    Parametres
    ----------
    w: str
        String a buscar en la llista
    f: list
        Llista d'strings en els que hem de buscar l'string w
        
    Retorna
    -------
    list
        Llista amb tots els strings posteriors a w en la llista f

    
    Tests públics (podeu posar els del Jutge)
    -------------
    >>> next_word_list('red', ['red','yellow','red','black','grey','red'])
    ['yellow', 'black']
    >>> next_word_list('big', ['small','big'])
    []
    >>> next_word_list('big' , ['big','small'])
    ['small']
    >>> next_word_list('blue', ['green'])
    []
    >>> next_word_list('blue', [])
    []
    >>> next_word_list('red', ['red','red','red'])
    ['red', 'red']
    
    Tests privats
    -------------
    >>> next_word_list('red', ['red'])
    []
    >>> next_word_list('',  ['red', 'blue'])
    []
    
    '''
    new_list=[]
    for i in range(len(f)):
        if f[i] == w and i + 1 < len(f):
            new_list.append(f[i + 1])
    return  new_list
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)