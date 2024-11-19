def saludo(n):
    """
    Paràmetres
    ----------
    n : hora
        Hora del dia (en format 24h)

    Retorna
    -------
    string
        Salutació corresponent a l'hora rebuda com a paràmetre

    Exemples públics
    ---------------
    >>> saludo(6)
    'Buenos dias'
    >>> saludo(18)
    'Buenas tardes'
    >>> saludo(23)
    'Buenas noches'
    
    Exemples privats
    ---------------
    >>> saludo(4)
    'Buenas noches'
    >>> saludo(12)
    'Buenas tardes'
    >>> saludo(21)
    'Buenas tardes'
    >>> saludo(5)
    'Buenos dias'
    >>> saludo(11)
    'Buenos dias'
    >>> saludo(22)
    'Buenas noches'
    """
    if n>=5 and n<12:
        return 'Buenos dias'
    elif n>=12 and n<22:
        return 'Buenas tardes'
    else:
        return 'Buenas noches'
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)