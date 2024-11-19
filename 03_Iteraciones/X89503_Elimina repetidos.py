def delete_repes(s):
    '''
    Paràmetres
    ----------

    s : string
        Cadena de caràcters que es vol netejar de repeticions.

    Retorna
    -------
    string
        Retorna un string amb els caràcters de s en el mateix ordre però sense caràcters repetits.

    Exemples públics
    ---------------
    >>> delete_repes('aaaa')
    'a'
    >>> delete_repes('hola')
    'hola'
    >>> delete_repes('aloha')
    'aloh'
    >>> delete_repes('1uno12dos123tres')
    '1uno2ds3tre'
    
    Exemples privats
    ----------------
    >>> delete_repes('')
    ''
    >>> delete_repes('abcde')
    'abcde'
    >>> delete_repes('aaabbbccc')
    'abc'
    >>> delete_repes('hello world')
    'helo wrd'
    >>> delete_repes('aaaabbbbcccc')
    'abc'
    >>> delete_repes('1234567890')
    '1234567890'
    '''

    not_repe = ''
    for i in s:
        if i not in not_repe:
            not_repe += i
    return not_repe


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)