def hay_cruces(M):
    '''
    Parametres
    ----------
    M: List
        Matriu de caràcters que conté símbols com "*" i "-". Precondició: M és una matriu rectangular.

    Retorna
    -------
    bool
        Retorna True si hi ha una creu (de un valor amb altres valors iguals en les quatre direccions adjacents), 
        i False en cas contrari.
    
    Tests públics
    -------------
    >>> M=[["-", "*", "-", "-"],
    ...    ["*", "*", "*", "*"],
    ...    ["-", "*", "-", "-"]]
    >>> hay_cruces(M)
    True
    >>> M=[["-", "-", "-"],
    ...    ["*", "*", "*"],
    ...    ["-", "*", "-"],
    ...    ["-", "-", "-"]]
    >>> hay_cruces(M)
    False

    Tests privats
    -------------
    >>> hay_cruces([["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]])
    True
    >>> hay_cruces([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
    False
    >>> hay_cruces([["*", "-", "*"], ["-", "*", "-"], ["*", "-", "*"]])
    False
    >>> hay_cruces([["*", "-", "*", "*"], ["*", "*", "*", "*"], ["*", "-", "*", "*"]])
    True
    '''
    for i in range(1, len(M) - 1):
        for j in range(1, len(M[0]) - 1):
            if (M[i][j]=="*" and M[i-1][j]=="*" and M[i+1][j]=="*"  and M[i][j-1]=="*" and M[i][j+1]=="*" and M[i-1][j-1]=="-" and M[i-1][j+1]=="-" and M[i+1][j-1]=="-" and  M[i+1][j+1]=="-"):
                return True
    
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)