def slow_pi_approx(n):
    '''
    Paràmetres
    ----------
    n : int
        Un enter no negatiu.

    Retorna
    -------
    float
        Una aproximació de pi arrodonida a quatre decimals.

    Tests públics
    -------------
    >>> slow_pi_approx(10)
    3.2323
    >>> slow_pi_approx(100)
    3.1515
    >>> slow_pi_approx(1000)
    3.1426

    Tests privats
    -------------
    >>> slow_pi_approx(500)
    3.1436
    >>> slow_pi_approx(2000)
    3.1421
    >>> slow_pi_approx(0)
    4.0
    '''

    approx = 0
    for k in range(n + 1):
        approx += ((-1) ** k) / (2 * k + 1)

    return round(4 * approx, 4)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)