"""
Given the dice values p and q got by the first player and r and s got by
the second player returns integer 1 if the winner is the first player,
returns 2 when the winner is the second player and returns integer 0 when
there is no winner. A player wins when his score does not exceed seven and
it is either closer to seven than the rival's score or the rival's score
exceeds seven (the player's score is the sum of the obtained values).
"""

def winner(p, q, r, s):
    '''
    Parameters
    ----------
    p : int
        The first dice value of the first player.
    q : int
        The second dice value of the first player.
    r : int
        The first dice value of the second player.
    s : int
        The second dice value of the second player.
        
    Returns
    -------
    int
        Returns integer 1 if the winner is the first player, returns 2
        when the winner is the second player and returns integer 0 when
        there is no winner.

    Public examples
    ---------------
    >>> winner(1, 3, 5, 3)
    1
    >>> winner(2, 4, 4, 3)
    2
    >>> winner(1, 3, 2, 3)
    2
    >>> winner(2, 4, 3, 3)
    0
    >>> winner(4, 4, 5, 6)
    0

    Private examples
    ---------------
    >>> winner(3, 3, 2, 2)
    1
    >>> winner(2, 2, 3, 3)
    2
    >>> winner(1, 1, 1, 1)
    0
    >>> winner(6, 6, 6, 6)
    0
    >>> winner(3, 4, 3, 4)
    0
    '''

    if p+q > r+s:
        if p+q <= 7:
            return 1
        elif r+s<= 7:
            return 2
        else:
            return 0
    elif r+s > p+q:
        if r+s <= 7:
            return 2
        elif p+q<= 7:
            return 1
        else:
            return 0
    else:
            return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)