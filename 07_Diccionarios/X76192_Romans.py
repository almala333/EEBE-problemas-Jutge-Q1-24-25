def romanos_a_int(rom):
    '''
    Parametres
    ----------
    rom: str
        Una cadena de caràcters que representa un número en numerals romans. 
        Precondicions: la cadena ha de ser vàlida i no buida.

    Retorna
    -------
    int
        El valor enter equivalent al número en numerals romans proporcionat.
    
    Tests públics
    -------------
    >>> romanos_a_int('MMMCMLXXXVI')
    3986


    Tests privats
    -------------
    >>> romanos_a_int('III')
    3
    >>> romanos_a_int('IV')
    4
    >>> romanos_a_int('IX')
    9
    >>> romanos_a_int('LVIII')
    58
    >>> romanos_a_int('MCMXCIV')
    1994
    '''
    values = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1,}
    total = 0
    prev_value = 0
    for char in rom: 
        if values[char] > prev_value:
            total += values[char] - 2 * prev_value  
        else:
            total += values[char]
        prev_value = values[char]
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)