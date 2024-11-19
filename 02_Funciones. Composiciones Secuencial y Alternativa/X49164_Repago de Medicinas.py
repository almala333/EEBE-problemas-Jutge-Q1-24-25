def repago(tipo, renta):
    '''
    Parámetros
    ----------
    tipo: str
        Tipo de usuario (Pensionista, Usuario, Sin subsidio, No contributiva, Integración, Accidente, Discapacidad)
    renta: int
        Renta del usuario

    Retorna
    -------
    Dos valores: el porcentaje de subsidio y el importe del subsidio

    Ejemplos públicos
    ---------------
    >>> repago('Pensionista', 5000)
    (10, 8.23)
    >>> repago('Pensionista', 180000)
    (60, 61.75)
    >>> repago('Usuario', 25000)
    (50, -1.0)
    >>> repago('Sin subsidio', 5000)
    (0, 0.0)

    Ejemplos privados
    ---------------
    >>> repago('Pensionista', 15000)
    (10, 8.23)
    >>> repago('Usuario', 100000)
    (60, -1.0)
    >>> repago('No contributiva', 20000)
    (0, 0.0)
    >>> repago('Accidente', 40000)
    (0, 0.0)
    >>> repago('Discapacidad', 50000)
    (0, 0.0)
    '''
    if ((tipo == 'Sin subsidio') or (tipo =='No contributiva') or (tipo == 'Integración') or (tipo== 'Accidente')  or (tipo == 'Discapacidad')):

     return(0, 0.0)
    elif (tipo=='Pensionista'):
        if (renta<18000):
            return (10, 8.23)
        elif (renta>=18000 and renta<100000):
            return (10, 18.52)
        else:
            return(60, 61.75)
    elif  (tipo=='Usuario'):
        if (renta<18000):
            return (40, -1.0)
        elif (renta>=18000 and renta<100000):
            return (50, -1.0)
        else:
            return(60, -1.0)
    else: 
        return('Dades no valides')

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)