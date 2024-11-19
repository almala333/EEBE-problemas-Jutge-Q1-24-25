def is_vowel_covered(s):
    '''
    Paràmetres
    ----------
    s: str
        Cadena de caràcters

    Retorna
    -------
    bool
        Cert si la cadena comença i acaba amb una vocal i té una vocal en la segona i penúltima posició, fals en cualsevol altre cas

    Tests públics
    ---------------
    >>> is_vowel_covered("AaaaA")
    True
    >>> is_vowel_covered("AaaA")
    False
    >>> is_vowel_covered("AeioUAeioU")
    True
    >>> is_vowel_covered("aAppAlAa")
    False
    >>> is_vowel_covered("AaaaaazZ")
    False

    Tests privats
    ---------------
    >>> is_vowel_covered("EeeEeE")
    True
    >>> is_vowel_covered("OoOoOo")
    False
    >>> is_vowel_covered("UuuUuU")
    True
    >>> is_vowel_covered("IiiIiI")
    True
    >>> is_vowel_covered("a")
    False
    >>> is_vowel_covered("")
    False
    '''
    if len(s) > 4 and (s[0] in 'AEIOU') and (s[-1] in 'AEIOU') and (s[1] in 'aeiou') and (s[-2] in 'aeiou'):
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)