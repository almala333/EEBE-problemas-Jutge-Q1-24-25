from math import sqrt


def sumdivisores(n):
    '''

    Paràmetres
    ----------
    n : int
        El nombre enter del qual es vol calcular la suma dels divisors propis.

    Retorna
    -------
    int
        La suma dels divisors propis de n.

    Tests públics
    -------------
    >>> sumdivisores(12)
    28
    >>> sumdivisores(220)
    504

    Tests privats
    -------------
    >>> sumdivisores(36)
    91
    >>> sumdivisores(42)
    96
    '''


    a = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
              a += i
            else:
                a += i + n // i

    return int(a)


def abundante(n):
    '''

    Paràmetres
    ----------
    n : int
        El nombre enter que es vol comprovar si és abundant.

    Retorna
    -------
    bool
        True si n és abundant, sino False.

    Tests públics
    -------------
    >>> abundante(40)
    True
    >>> abundante(45)
    False

    Tests privats
    -------------
    >>> abundante(60)
    True
    >>> abundante(66)
    True
    '''


    if( sumdivisores(n) > 2*n ): 
        return True
    else: 
        return False


def abundantes_consecutivos(desde, hasta):
    '''
    Paràmetres
    ----------
    desde : int
        El límit inferior del rang de nombres a comprovar.
    hasta : int
        El límit superior del rang de nombres a comprovar.

    Retorna
    -------
    int
        El nombre de parells de nombres enters consecutius que són abundants.

    Tests públics
    -------------
    >>> abundantes_consecutivos(5000, 10000)
    3

    Tests privats
    -------------
    >>> abundantes_consecutivos(1000, 2000)
    0
    >>> abundantes_consecutivos(3000, 4000)
    0
    '''


    a = 0
    for i in range(desde, hasta):
        if( abundante(i) and abundante(i+1)): 
            a += 1

    return a


def primer_consecutivo(desde, hasta):
    '''
    Paràmetres
    ----------
    desde : int
        El límit inferior del rang de nombres a comprovar.
    hasta : int
        El límit superior del rang de nombres a comprovar.

    Retorna
    -------
    int
        El primer nombre enter que forma un parell de nombres consecutius amb el següent nombre, tots dos sent abundants. Si no es troba cap, retorna -1.

    Tests públics
    -------------
    >>> primer_consecutivo(5000, 10000)
    5775
    >>> primer_consecutivo(6000, 7000)
    -1

    Tests privats
    -------------
    >>> primer_consecutivo(2000, 3000)
    -1
    >>> primer_consecutivo(4000, 5000)
    -1
    '''


    for i in range(desde, hasta):
        if( abundante(i) and abundante(i+1) ): 
            return i

    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)