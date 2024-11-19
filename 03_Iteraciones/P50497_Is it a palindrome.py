def is_palindrome(s: str) -> bool:
    '''
    Parameters
    ----------
    s : str
        La cadena a comprovar si és un palindrome.
    
    Returns
    -------
    bool
        True si la cadena és un palindrome, False altrament.
    
    Tests públics
    -------------
    >>> is_palindrome("anna")
    True
    >>> is_palindrome("abc")
    False
    
    Tests privats
    -------------
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    '''
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)