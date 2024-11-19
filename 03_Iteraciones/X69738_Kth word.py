def kth_word(s, k):
    '''
    Parametres
    ----------
    s: str
        La cadena de text que conté les paraules.
    k: int
        El número de la paraula que es vol obtenir.

    Retorna
    -------
    str
        La paraula numero k de la cadena de text, o una cadena buida si no existeix.

    Tests públics
    -------------
    >>> kth_word('Alea iacta est', 3)
    'est'
    >>> kth_word('Alea iacta est', 1)
    'Alea'
    >>> kth_word('KingKong', 2)
    ''

    Tests privats
    -------------
    >>> kth_word('Hola món', 2)
    'món'
    >>> kth_word('Això és un exemple', 4)
    'exemple'
    >>> kth_word('Bon dia', 3)
    ''
    
    '''
    
    word_count = 0
    word = ''
    for i in s:
        if i == ' ':
            if word:
                word_count += 1
                if word_count == k:
                    return word
                else: 
                    word = ''
        else:
            word += i
    if word:
        word_count += 1
        if word_count == k:
            return word
    return ''
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)