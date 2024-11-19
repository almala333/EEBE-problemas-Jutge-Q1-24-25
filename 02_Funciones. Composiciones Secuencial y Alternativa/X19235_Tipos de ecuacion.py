def tipo_quad(a, b, c):
    '''
    Paràmetres
    ----------
    a : coeficient cuadràtic
        Coeficient del terme cuadràtic de la funció
    b : coeficient lineal
        Coeficient del terme lineal de la funció
    c : terme independent
        Terme independent de la funció

    Retorna
    -------
    string
        Tipus de funció cuadràtica (constante, lineal, cuadràtica pura, cuadràtica mixta o cuadràtica completa)

    Exemples públics
    ---------------
    >>> tipo_quad(0, 0, 4)
    'constante'
    >>> tipo_quad(0, 2, 4)
    'lineal'
    >>> tipo_quad(3, 0, 2)
    'cuadratica pura'
    >>> tipo_quad(3, 2, 0)
    'cuadratica mixta'
    >>> tipo_quad(2, 3, 4)
    'cuadratica completa'
    >>> tipo_quad(4, 0, 1)
    'cuadratica pura'
    >>> tipo_quad(4, 2, 1)
    'cuadratica completa'
    
    Exemples privats
    ---------------
    >>> tipo_quad(0, 0, 0)
    'constante'
    >>> tipo_quad(0, 3, 0)
    'lineal'
    >>> tipo_quad(2, 0, 0)
    'cuadratica pura'
    >>> tipo_quad(2, 3, 0)
    'cuadratica mixta'
    >>> tipo_quad(2, 0, 3)
    'cuadratica pura'
    
    '''
    if a==0:
        if b==0:
            return 'constante'
        else:
            return 'lineal'
    elif b==0:
        return 'cuadratica pura'
    elif c==0:
        return 'cuadratica mixta'
    else:
        return 'cuadratica completa'
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)