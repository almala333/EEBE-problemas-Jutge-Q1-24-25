def max_altura(s):
    '''
    Parametres
    ----------
    s : str
        Cadena de caràcters '+' i '-' que representen la cuantitaat de plats que es posen i treuen.

    Retorna
    -------
    int
        L'altura assolida.

    Tests públics 
    -------------
    >>> max_altura('+++--+')
    3
    >>> max_altura('+-+-+-')
    1
    >>> max_altura('++-+++--+')
    4
    
    Tests privats
    -------------
    >>> max_altura('')
    0
    >>> max_altura('+++++')
    5
    >>> max_altura('-----')
    0
    >>> max_altura('-+-+-+')
    1
    >>> max_altura('++--++')
    2
    
    '''
    count = 0
    max = 0
    for i in s:
        if i == '+':
            count += 1
        elif i == '-' and count>0:
            count -= 1
        if( count > max): max = count
    return max

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)