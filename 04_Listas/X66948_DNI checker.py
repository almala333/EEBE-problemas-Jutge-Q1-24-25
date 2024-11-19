def check_letter(num, letra):
    return letra == 'TRWAGMYFPDXBNJZSQVHLCKE'[num%23]

def busca_dni(lista):
    '''
    Parametres
    ----------
    lista : list
        Llista de DNIs a verificar.

    Retorna
    -------
    str
        'ok' si tots els DNI són vàlids, el primer DNI invàlid en cas contrari.
    
    Tests públics 
    -------------
    >>> busca_dni(['12345678Z', '98765432M'])
    'ok'
    >>> busca_dni(['44556677A', '98765432M'])
    '44556677A'
    >>> busca_dni(['37485960P', '150150150', '13243546P'])
    '150150150'
    >>> busca_dni(['123456S', '13243546P'])
    '123456S'
    >>> busca_dni(['98765432M', '1234567890H'])
    '1234567890H'
    
    Tests privats
    -------------
    >>> busca_dni(['12345678Z', '98765432M', '12345678Z'])
    'ok'
    >>> busca_dni(['44556677A', '12345678Z', '98765432M'])
    '44556677A'
    >>> busca_dni(['37485960P', '150150150', '13243546P', '12345678Z'])
    '150150150'
    >>> busca_dni(['123456S', '13243546P', '98765432M'])
    '123456S'
    >>> busca_dni(['98765432M', '1234567890H', '12345678Z'])
    '1234567890H'
    >>> busca_dni(['12345678Z', '12345678Z', '12345678Z'])
    'ok'
    >>> busca_dni(['44556677A', '44556677A', '98765432M'])
    '44556677A'
    '''
    for dni in lista:
        if len(dni) != 9:
            return dni
        num_part = dni[:-1]  
        letter_part = dni[-1] 
        if not num_part.isdigit():
            return dni
        num = int(num_part)
        if not check_letter(num, letter_part):
            return dni
    return "ok"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)