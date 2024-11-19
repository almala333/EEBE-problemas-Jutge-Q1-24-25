def word_count(s):
    '''
    Paràmetres
    ----------
    text: str
        Cadena de caràcters que es vol comptar les paraules.

    Retorna
    -------
    int
        El nombre de paraules que hi ha a la cadena de caràcters.

    Tests públics 
    -------------
    >>> word_count('Qui invenit amicum invenit thesaurum')
    5
    >>> word_count('alea iacta          est')
    3
    >>> word_count('KingKong')
    1

    Tests privats
    -------------
    >>> word_count('Això és una prova')
    4
    >>> word_count('   ')
    0
    >>> word_count('Una sola paraula')
    3
    >>> word_count('Paraules    separades  per  múltiples      espais')
    5
    >>> word_count('Una frase amb punt final.')
    5
    >>> word_count('')
    0
    '''

    compte = 0
    paraula = False
    for i in s:
        if i == ' ':
            paraula = False
        else:
            if not paraula:
                compte += 1
                paraula = True
    return compte

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)