def codi(s):
    '''
    Paràmetres
    ----------
    s: str
        Cadena de caràcters que conté el nom i cognoms d'una persona.

    Retorna
    -------
    str
        Una cadena que conté les inicials del nom i cognoms seguides del nombre de caràcters que té la cadena original.

    Tests públics 
    -------------
    >>> codi('Mireia Belmonte Garcia')
    'MBG20'
    >>> codi('Bruce Frederick Joseph Springsteen')
    'BFJS31'
    >>> codi('')
    ''

    Tests privats
    -------------
    >>> codi('Pere Puig i Pla')
    'PPP12'
    >>> codi('Anna Maria Riera i Soler')
    'AMRS20'
    >>> codi('Joan Pere')
    'JP8'
    >>> codi('Maria del Mar')
    'MM11'
    >>> codi('  ')
    ''
    '''
    count  = 0
    ini = ''
    for i in s:
        if i.isupper():
            ini += i
            count += 1
        elif i.islower():
            count += 1
    if count != 0:
        count = str(count)
        data = ini + count
        return data
    else:
        return ''
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)