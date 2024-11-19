def nou_string(s, x):
    '''
    Paràmetres
    ----------
    s : string
        La cadena original.
    x : int
        El nombre de vegades que es repeteix cada vocal.

    Retorna
    -------
    string
        La cadena resultant de repetir cada vocal de s exactament x vegades
        en el lloc on es troba situada a s.

    Exemples públics
    ---------------
    >>> nou_string('Chewbacca', 2)
    'Cheewbaaccaa'
    >>> nou_string('R2-D2', 1)
    'R2-D2'
    >>> nou_string('C-3PO', 3)
    'C-3POOO'

    Exemples privats
    ----------------
    >>> nou_string('Hola mon', 2)
    'Hoolaa moon'
    >>> nou_string('Python', 3)
    'Pythooon'
    >>> nou_string('123', 4)
    '123'
    '''

    new = ''
    for i in s:
        if i in 'aeiouAEIOU':
            new += i*x
        else:
            new += i
    return new


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)