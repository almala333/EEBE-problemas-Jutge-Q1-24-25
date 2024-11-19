def suma_qext(mat):
    '''
    Paràmetres
    ----------
    mat: list
        Representació en una llista d'una matriu

    Retorna
    -------
    int
        Numero total que sumen els valors exteriors de la matriu
    
    Tests públics 
    --------------
    >>> mat = [[5,6,4,7,3],[9,3,7,4,2],[7,3,4,8,2],[2,3,6,2,2],[6,7,1,1,6]]
    >>> suma_qext(mat)
    70
    >>> m = [[4, 4, 4], [4, 2, 9], [7, 2, 7], [1, 2, 3]]
    >>> suma_qext(m)
    45
    >>> suma_qext([[1,1],[2,2]])
    6
    
    Tests privats
    -------------
    >>> suma_qext([])
    0
    >>> suma_qext([[1,2,3],[4,5,6],[7,8,9]])
    45
    >>> suma_qext([[10],[20],[30]])
    60
    '''
    
    amount=0
    if len(mat)==0 or len(mat[0])==0:
        return amount
    amount+=sum(mat[0])
    amount+=sum(mat[-1])
    
    for i in range(1, len(mat) - 1):
        amount += mat[i][0] + mat[i][-1]
    
    return amount

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)