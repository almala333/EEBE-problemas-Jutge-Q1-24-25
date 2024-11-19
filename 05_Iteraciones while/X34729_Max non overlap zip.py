def max_non_overlap_zip(s, t):
    '''
    Parametres
    ----------
    s: str
        Primer string
    t:str
        Segon string

    Retorna
    -------
    Un string que compleixi els requisits de zip
    
    Tests públics 
    -------------
    >>> max_non_overlap_zip("abcbdz", "baccu")
    'abba'
    >>> max_non_overlap_zip("abcbdz", "abccu")
    ''
    >>> max_non_overlap_zip("abcbdz", "bccu")
    'abbc'
    >>> max_non_overlap_zip("abxcbdz", "cdhcu")
    'acbdxh'


    Tests privats
    -------------
    >>> max_non_overlap_zip("abc", "def")
    'adbecf'
    >>> max_non_overlap_zip("aaa", "bbb")
    'ababab'
    >>> max_non_overlap_zip("abcdef", "fedcba")
    'afbecddcebfa'
    >>> max_non_overlap_zip("abcdef", "abcdef")
    ''
    >>> max_non_overlap_zip("abcdef", "abcxyz")
    ''
    >>> max_non_overlap_zip("abcdef", "xabcde")
    'axbacbdcedfe'
    >>> max_non_overlap_zip("aaabbbccc", "dddeeefff")
    'adadadbebebecfcfcf'
    
    '''
    prefix_length = 0
    while prefix_length < min(len(s), len(t)) and s[prefix_length] != t[prefix_length]:
        prefix_length += 1

    if prefix_length == 0:
        return ''

    s_prefix = s[:prefix_length]
    t_prefix = t[:prefix_length]

    result = ''
    for i in range(prefix_length):
        result += s_prefix[i] + t_prefix[i]

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    