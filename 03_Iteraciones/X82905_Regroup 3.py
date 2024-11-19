def regroup(s):
    """
    Paràmetres
    ----------
    s : string
        La cadena que es vol reagrupar
        
    Retorna
    -------
    string   
        Retorna una reagrupació dels caràcters
        en la cadena s. La reagrupació és la següent:
        en la cadena retornada, primer venen les
        lletres, en el mateix ordre que van venir
        en la cadena argument; i després venen els
        dígits, en el mateix ordre que van venir
        en la cadena argument.

    Exemples públics
    ---------------  
    >>> regroup('r2b2')
    'rb22'
    >>> regroup('a45tr09pw')
    'atrpw4509'
    >>> regroup('nonumbers')
    'nonumbers'
    >>> regroup('543210')
    '543210'
    
    Exemples privats
    ----------------
    >>> regroup('abc123def456')
    'abcdef123456'
    >>> regroup('123abc456def')
    'abcdef123456'
    >>> regroup('a1b2c3d4e5f6')
    'abcdef123456'
    >>> regroup('123')
    '123'
    >>> regroup('abc')
    'abc'
    >>> regroup('')
    ''
    >>> regroup('a1b2c3!@#d4e5f6')
    'abcdef123456'
    """
    letter = ''
    digit = ''
    for i in s:
      if i.isalpha():
          letter += i
      elif i.isdigit():
          digit += i
    return letter + digit


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)