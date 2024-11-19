def int_root(n):
    '''
    Parametres
    ----------
    n: int
        Un nombre enter no negatiu del qual es vol calcular la arrel sencera.

    Retorna
    -------
    int
        L'arrel sencera més gran que no excedeix n.
    
    Tests públics 
    -------------
    >>> int_root(19)
    4

    Tests privats
    -------------
    >>> int_root(0)
    0
    >>> int_root(1)
    1
    >>> int_root(25)
    5
    >>> int_root(50)
    7
    
    '''

    k = 0
    while (k + 1) * (k + 1) <= n:
        k += 1
    return k

def int_log(a, b):
    '''
    Parametres
    ----------
    a: int
        La base del logaritme, ha de ser un nombre enter positiu.
    b: int
        El nombre enter del qual es vol calcular el logaritme en base a.

    Retorna
    -------
    int
        El logaritme enter més gran que no excedeix b en base a.
    
    Tests públics 
    -------------
    >>> int_log(3, 20)
    2

    Tests privats
    -------------
    >>> int_log(2, 16)
    4
    >>> int_log(5, 100)
    2
    >>> int_log(10, 1000)
    3
    >>> int_log(4, 64)
    3
    
    '''

    k = 0
    power = 1  
    while power <= b:
        k += 1
        power *= a
    return k - 1

def gcd_lcm(a, b):
    '''
    Parametres
    ----------
    a: int
        Un nombre enter positiu.
    b: int
        Un nombre enter positiu.

    Retorna
    -------
    tuple
        Un tupla que conté el màxim comú divisor (gcd) i el mínim comú múltiple (lcm) dels dos nombres.
    
    Tests públics
    -------------
    >>> gcd_lcm(12, 18)
    (6, 36)

    Tests privats
    -------------
    >>> gcd_lcm(15, 25)
    (5, 75)
    >>> gcd_lcm(7, 3)
    (1, 21)
    >>> gcd_lcm(8, 12)
    (4, 24)
    >>> gcd_lcm(1, 1)
    (1, 1)
    
    '''
   
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    gcd_value = gcd(a, b)
    lcm_value = (a // gcd_value) * b 
    return gcd_value, lcm_value


def is_prime(n):
    '''
    Parametres
    ----------
    n: int
        Un nombre enter no negatiu del qual es vol determinar si és primer.

    Retorna
    -------
    bool
        Retorna True si n és un nombre primer, False en cas contrari.
    
    Tests públics 
    -------------
    >>> is_prime(51)
    False

    Tests privats
    -------------
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(29)
    True
    >>> is_prime(1)
    False
    '''

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def buy_tokens(n):
    '''
    Parametres
    ----------
    n: int
        Un nombre enter positiu que representa la quantitat total de diners disponibles per comprar tokens.

    Retorna
    -------
    tuple
        Una tupla que conté el nombre òptim de tokens vermells i grocs que es poden comprar amb la quantitat de diners donada.
    
    Tests públics 
    -------------
    >>> buy_tokens(50)
    (6, 2)

    Tests privats
    -------------
    >>> buy_tokens(0)
    (0, 0)
    >>> buy_tokens(7)
    (1, 0)
    >>> buy_tokens(28)
    (4, 0)
    >>> buy_tokens(40)
    (4, 3)
    >>> buy_tokens(110)
    (14, 3)
    '''

    best_red = 0
    best_yellow = n//4+1  
    
    red_tokens = 0
    while red_tokens*7 <= n:
        remaining = n-(red_tokens*7)
        
        if remaining%4 == 0:
            yellow_tokens = remaining//4
            total_tokens = red_tokens+yellow_tokens
            
            if total_tokens<(best_red+best_yellow):
                best_red = red_tokens
                best_yellow = yellow_tokens        
        red_tokens += 1
    return (best_red, best_yellow)


def inv_factorial(n):
    '''
    Parametres
    ----------
    n: int
        Un nombre enter positiu que representa el valor del factorial que es vol invertir.

    Retorna
    -------
    int
        El nombre enter més petit tal que el seu factorial sigui igual o superior a n.
    
    Tests públics 
    -------------
    >>> inv_factorial(50)
    5

    Tests privats
    -------------
    >>> inv_factorial(1)
    1
    >>> inv_factorial(6)
    3
    >>> inv_factorial(24)
    4
    >>> inv_factorial(120)
    5
    >>> inv_factorial(720)
    6
    '''

    m = 1
    factorial = 1
    
    while factorial < n:
        m += 1
        factorial *= m
        
    return m

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

