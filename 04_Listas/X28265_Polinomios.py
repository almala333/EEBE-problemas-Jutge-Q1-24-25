def derivada(p):
    '''
    >>> derivada([-1, 5, -2, 3])
    [5, -4, 9]
    
    '''
    
    deriv_func = []
    for i in range(len(p)):
        if i != 0:
            deriv_func.append(i*int(p[i]))
    return deriv_func
def producto_monomio(p, m):
    '''
    >>> producto_monomio([1,3,2], [0,0,0,0,3])
    [0, 0, 0, 0, 3, 9, 6]
    '''
    n = m[:-1]
    for i in p:
        n.append(i*m[-1])
    return n
def suma(p, q):
    '''
    >>> suma([1, 1], [-2, -1, 0, 3])
    [-1, 0, 0, 3]
    >>> suma([2, 1, -1, 2], [-1, 1, 1, -2])
    [1, 2]
    >>> suma([0, 1], [0, -1])
    []
    '''
    sum_pol = []
    len_diff = len(p) - len(q)
    for i in range(min(len(p), len(q))):
        sum_pol.append(p[i] + q[i])
    if len_diff > 0:
        sum_pol.extend(p[min(len(p), len(q)):])
    elif len_diff < 0:
        sum_pol.extend(q[min(len(p), len(q)):])
    else:
        for i in range(len(sum_pol)-1, -1, -1):
            if sum_pol[i] != 0:
                return sum_pol[:i+1]
        return []
    return sum_pol


def producto (p,q):
    '''
    >>> producto([1, 1], [1, -1])
    [1, 0, -1]
    >>> producto([2, 0, 1], [1, -1, 1, 2])
    [2, -2, 3, 3, 1, 2]
    >>> producto([1, 2, 3, 4], [-1])
    [-1, -2, -3, -4]
    '''
    result = [0] * (len(p) + len(q) - 1)

    for i in range(len(q)):
        monomio = [0] * i + [q[i]] 
        producto_m = producto_monomio(p, monomio)  
        result = suma(result, producto_m)
    for i in range(len(result)-1, -1, -1):
        if result[i] != 0:
            return result[:i+1]
        return []
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)