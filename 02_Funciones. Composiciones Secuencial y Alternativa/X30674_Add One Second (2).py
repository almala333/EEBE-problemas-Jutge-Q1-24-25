def add1sec(h, m, s):
    '''
    Parameters
    ----------
    h: int
        The hour of the clock time
    m: int
        The minute of the clock time
    s: int
        The second of the clock time

    Returns
    -------
    (int, int, int)
        Returns in hours, minutes and seconds, the clock time
        increased by one second. The resulting clock time obey the
        same inequalities than the arguments.
    
    Public examples
    ---------------
    >>> add1sec(0, 1, 2)
    (0, 1, 3)
    >>> add1sec(3, 5, 9)
    (3, 5, 10)
    >>> add1sec(19, 45, 59)
    (19, 46, 0)
    >>> add1sec(12, 59, 59)
    (13, 0, 0)

    Private examples
    ---------------
    >>> add1sec(9, 30, 45)
    (9, 30, 46)
    >>> add1sec(6, 0, 0)
    (6, 0, 1)
    >>> add1sec(0, 0, 0)
    (0, 0, 1)
    >>> add1sec(10, 59, 59)
    (11, 0, 0)
    >>> add1sec(23, 0, 0)
    (23, 0, 1)
    >>> add1sec(12, 30, 0)
    (12, 30, 1)

    '''
    s = s+1
    if s == 60:
        s = 0
        m = m+1
        if m==60:
            m=0
            h=h+1
            if h==24:
                h=0
    return (h, m, s)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)