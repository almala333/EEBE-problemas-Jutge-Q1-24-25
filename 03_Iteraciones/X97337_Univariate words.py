def is_univariate_word(s):
    '''
    Parametres
    ----------
    s : str
        Cadena de caràcters a comprovar.

    Retorna
    -------
    bool
        True si tots els caràcters de la cadena són iguals, False en cas contrari.

    Tests públics 
    -------------
    >>> is_univariate_word('xxXxxxXX')
    True
    >>> is_univariate_word('xyyyyYYY')
    False
    >>> is_univariate_word('y')
    True
    >>> is_univariate_word('yyyyx')
    False

    Tests privats
    -------------
    >>> is_univariate_word('aaaa')
    True
    >>> is_univariate_word('abcde')
    False
    >>> is_univariate_word('AaAaAa')
    True
    >>> is_univariate_word('12345')
    False
    '''

    first_letter = s[0]
    condition = True
    if first_letter.isupper():
        first_letter = first_letter.lower()
    for letter in s:
        if letter.lower() != first_letter:
            condition = False         
    return condition

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)