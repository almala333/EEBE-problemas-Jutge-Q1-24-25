def histograma_h(lis):
    '''
    Parametres
    ----------
    lis: llista d'enters
        Llista de nombres enters per als quals es vol calcular el histograma.

    Retorna
    -------
    No retorna cap valor, però imprimeix el histograma de freqüències dels elements de la llista.
    
    Tests públics
    -------------
    >>> histograma_h([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
    1 *****
    2 ******
    3 ****
    4 **

    Tests privats
    -------------
    >>> histograma_h([5, 5, 5, 1, 1, 2])
    1 **
    2 *
    5 ***
    
    >>> histograma_h([7, 8, 9, 7, 8, 7])
    7 ***
    8 **
    9 *

    >>> histograma_h([10, 10, 10, 10])
    10 ****
    '''
    fr = {}
    for i in lis:
        if i in fr:
            fr[i] += 1
        else:
            fr[i] = 1
    sorted_keys = sorted(fr.keys())
    for key in sorted_keys:
        print(f"{key} {'*' * fr[key]}")

def histograma_v(lis):
    '''
    Parametres
    ----------
    lis: llista d'enters
        Llista de nombres enters per als quals es vol calcular el histograma vertical.

    Retorna
    -------
    No retorna cap valor, però imprimeix el histograma vertical de freqüències dels elements de la llista.
    
    Tests públics
    -------------
    >>> histograma_v([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
      *     
    * *     
    * * *   
    * * *   
    * * * * 
    * * * * 
    1 2 3 4 

    '''
    fr = {}
    for i in lis:
        if i in fr:
            fr[i] += 1
        else:
            fr[i] = 1
    sorted_keys = sorted(fr.keys())
    max_freq = max(fr.values())
    for level in range(max_freq, 0, -1):
        line = ''
        for key in sorted_keys:
            if fr[key] >= level:
                line += '* '
            else:
                line += '  '
        print(line)
    legend = ' '.join(str(key) for key in sorted_keys)
    legend += ' '
    print(legend)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)