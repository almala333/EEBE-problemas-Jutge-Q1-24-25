def nmultiplos(num_inicial, num_final, num_multiples):
    '''
    Parametres
    ----------
    num_inicial: int
        El número inicial de la seqüència.
    num_final: int
        El número final de la seqüència.
    num_multiples: int
        El nombre de múltiplos a calcular per cada número de la seqüència.

    Retorna
    -------
    Una cadena que conté les taules de múltiplos dels números de la seqüència.

    Tests públics (podeu posar els del Jutge)
    -------------
    >>> nmultiplos(1, 5, 10)
    1 2 3 4 5 6 7 8 9 10
    2 4 6 8 10 12 14 16 18 20
    3 6 9 12 15 18 21 24 27 30
    4 8 12 16 20 24 28 32 36 40
    5 10 15 20 25 30 35 40 45 50
    >>> nmultiplos(20, 30, 5)
    20 40 60 80 100
    21 42 63 84 105
    22 44 66 88 110
    23 46 69 92 115
    24 48 72 96 120
    25 50 75 100 125
    26 52 78 104 130
    27 54 81 108 135
    28 56 84 112 140
    29 58 87 116 145
    30 60 90 120 150

    Tests privats
    -------------
    >>> nmultiplos(5, 10, 3)
    5 10 15
    6 12 18
    7 14 21
    8 16 24
    9 18 27
    10 20 30
    >>> nmultiplos(15, 20, 4)
    15 30 45 60
    16 32 48 64
    17 34 51 68
    18 36 54 72
    19 38 57 76
    20 40 60 80
    '''
    res = ''

    for k in range(num_inicial, num_final+1 ):
        for m in range(1, num_multiples+1):
            res += str(m*k)
            if(m != num_multiples): res += ' '
        print(res)
        res = ''
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)