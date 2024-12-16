def sum_of_digits_sorted(numbers):
    '''
    Paràmetres
    ----------
    numbers: list
        Llista de números enters.

    Retorna
    -------
    list
        Llista de números ordenats segons la suma dels seus dígits.

    Tests públics
    -------------
    >>> sum_of_digits_sorted([56, 2131])
    [2131, 56]
    >>> sum_of_digits_sorted([313, 44, 36, 11111, 35, 26, 7])
    [11111, 7, 313, 26, 35, 44, 36]
    >>> sum_of_digits_sorted([9, 53, 511, 4000, 10001, 45])
    [10001, 4000, 511, 53, 9, 45]

    Tests privats
    -------------
    >>> sum_of_digits_sorted([123, 456, 789])
    [123, 456, 789]
    >>> sum_of_digits_sorted([10, 20, 30])
    [10, 20, 30]
    >>> sum_of_digits_sorted([5, 5, 5])
    [5, 5, 5]
    '''
    
    
    def sort_key(x):
        digit_sum = 0
        for d in str(x):
            digit_sum += int(d)
        return (digit_sum, x)

    return sorted(numbers, key=sort_key)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
