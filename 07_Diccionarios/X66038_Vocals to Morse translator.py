def morse_vowel_translator(dic_morse_vow, s):
    '''
    Parametres
    ----------
    dic_morse_vow : dict
        Un diccionari que conté les corresponents representacions en codi Morse per a les vocals majúscules.
    s : str
        Una cadena de text que pot contenir vocals (majúscules o minúscules) i altres caràcters.

    Retorna
    -------
    str
        Una cadena que conté la representació en codi Morse de les vocals majúscules presents a la cadena d'entrada,
        separades per espais. Si no hi ha vocals majúscules, retorna una cadena buida.
    
    Tests públics
    -------------
    >>> dic_morse_vow = {"A":".-","E":".","I":"..","O":"---", "U":"..-"}
    >>> morse_vowel_translator(dic_morse_vow,"LALALAlalala")
    '.- .- .-'
    >>> morse_vowel_translator(dic_morse_vow,"AaEeIiOoUu")
    '.- . .. --- ..-'
    >>> morse_vowel_translator(dic_morse_vow,"aeiou")
    ''
    >>> morse_vowel_translator(dic_morse_vow,"UOIAE")
    '..- --- .. .- .'
    >>> morse_vowel_translator(dic_morse_vow,"AIAIAIAI")
    '.- .. .- .. .- .. .- ..'
    >>> morse_vowel_translator(dic_morse_vow,"A")
    '.-'
    >>> morse_vowel_translator(dic_morse_vow,"E")
    '.'
    >>> morse_vowel_translator(dic_morse_vow,"I")
    '..'
    >>> morse_vowel_translator(dic_morse_vow,"O")
    '---'
    >>> morse_vowel_translator(dic_morse_vow,"U")
    '..-'

    Tests privats
    -------------
    >>> morse_vowel_translator(dic_morse_vow,"HELLO")
    '. ---'
    >>> morse_vowel_translator(dic_morse_vow,"WORLD")
    '---'
    >>> morse_vowel_translator(dic_morse_vow,"AEIOU")
    '.- . .. --- ..-'
    >>> morse_vowel_translator(dic_morse_vow,"AaBbCc")
    '.-'
    >>> morse_vowel_translator(dic_morse_vow,"AABBAA")
    '.- .- .- .-'
    '''

    capital_vowels = []
    for char in s:
        if char in dic_morse_vow:
            capital_vowels.append(char)
    morse_code = []
    for vowel in capital_vowels:
        morse_code.append(dic_morse_vow[vowel])
    result = ''
    for code in morse_code:
        if result:  
            result += ' '
        result += code
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)