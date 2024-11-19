def vowel_consonant_count(s):
    """
    Paràmetres
    ----------
    s : str
        La cadena que es vol comptar.

    Retorna
    -------
    Un parell de valors que conté el nombre de vocals i consonants que apareixen a la cadena s.
        
    Public examples
    ---------------
    >>> vowel_consonant_count('SpartacUs')
    (3, 6)
    >>> vowel_consonant_count('KingKong')
    (2, 6)

    Private examples
    ----------------
    >>> vowel_consonant_count('Hello World')
    (3, 7)
    >>> vowel_consonant_count('AEIOU')
    (5, 0)
    >>> vowel_consonant_count('bcdfghjklmnpqrstvwxyz')
    (0, 21)
    >>> vowel_consonant_count('')
    (0, 0)
    >>> vowel_consonant_count('1234567890')
    (0, 0)
    >>> vowel_consonant_count('!@#$%^&*()')
    (0, 0)
    
    """
    vowel_count = 0
    consonant_count = 0
    for i in s:
       if i in 'AEIOUaeiouÀÈÌÒÙàèìòù':
         vowel_count += 1
       elif i.isalpha():
         consonant_count += 1
    return (vowel_count, consonant_count)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)