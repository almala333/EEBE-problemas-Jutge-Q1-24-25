def is_sun_extension(s):
    '''
    Parametres
    ----------
    s: str
        Cadena de caràcters a comprovar si conté nomes tenint en compte les lletres s, u, n "sun".

    Retorna
    -------
    bool
        True si la cadena amb nomes s, u, n conté "sun", False en cas contrari.

    Tests públics 
    -------------
    >>> is_sun_extension('sun')
    True
    >>> is_sun_extension('assumption')
    True
    >>> is_sun_extension('assume')
    False
    >>> is_sun_extension('russian')
    False
    >>> is_sun_extension('scouting')
    True
    >>> is_sun_extension('innocuous')
    False

    Tests privats
    -------------
    >>> is_sun_extension('sunny')
    True
    >>> is_sun_extension('sunflower')
    True
    >>> is_sun_extension('hello')
    False
    >>> is_sun_extension('')
    False
    '''
    new_str = ''

    for i in s.lower():
        if( i=='s' and new_str=='' ): 
            new_str += i

        if( i=='u' and new_str=='s' ):
            new_str += i

        if( i=='n' and new_str=='su' ):
            new_str += i

    if( new_str == 'sun' ):
        return True

    else: 
        return False



    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)