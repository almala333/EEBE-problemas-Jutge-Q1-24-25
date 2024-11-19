def empty_triangle(alçada):
    '''
    Paràmetres
    ----------
    alçada : int
        Alçada del triangle buit.

    Retorna
    -------
    No retorna res, només imprimeix el triangle buit per pantalla.

    Tests públics
    -------------
    >>> empty_triangle(3)
      *
     * *
    *****
    >>> empty_triangle(5)
        *
       * *
      *   *
     *     *
    *********
    
    Tests privats
    -------------
    >>> empty_triangle(9)
            *
           * *
          *   *
         *     *
        *       *
       *         *
      *           *
     *             *
    *****************
    
    '''
    for i in range(1, alçada+1):
        if i == 1:
            print(' ' * (alçada - i) + '*')
        elif i != alçada:
            print(' ' * (alçada - i) + '*' + ' ' * (2 * i - 3) + '*')
        else:
            print('*' * (2 * i - 1))
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

