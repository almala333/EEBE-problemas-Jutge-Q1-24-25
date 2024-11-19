def delete_digits(s):
    """
    Parameters
    ----------
    s : string
        La cadena original que es vol processar.
    
    Returns
    -------
    string
        Returns the string obtained after
        ruling out the digit characters
        of string s.

    Public examples
    ---------------
    >>> delete_digits('#Pelham 1-2-3#')
    '#Pelham --#'
    >>> delete_digits('7 up')
    ' up'
    >>> delete_digits('92920')
    ''
    
    Private examples
    ----------------
    >>> delete_digits('Hello World')
    'Hello World'
    >>> delete_digits('123abc456')
    'abc'
    >>> delete_digits('')
    ''
    >>> delete_digits('abcdefg')
    'abcdefg'
    >>> delete_digits('123456')
    ''
    >>> delete_digits('abc123def456')
    'abcdef'
    >>> delete_digits('123abc')
    'abc'
    >>> delete_digits('abc123')
    'abc'
    """
    new=''
    for i in s:
        if i.isdigit() != True:
            new += i
    return new
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
