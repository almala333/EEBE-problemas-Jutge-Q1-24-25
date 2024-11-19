def compta_atoms(compost):
    '''
    Parametres
    ----------
    compost : str
        Una cadena que representa un compost químic.

    Retorna
    -------
    int
        El nombre total d'àtoms en el compost.

    Tests públics (podeu posar els del Jutge)
    -------------
    >>> compta_atoms('HIO')
    3
    >>> compta_atoms('H2O')
    3
    >>> compta_atoms('C2H5O')
    8
    >>> compta_atoms('CaCO3')
    5
    >>> compta_atoms('Fe3O4')
    7

    Tests privats
    -------------
    >>> compta_atoms('CH4')
    5
    >>> compta_atoms('CO2')
    3
    >>> compta_atoms('H2SO4')
    7
    >>> compta_atoms('NaCl')
    2
    >>> compta_atoms('Al2O3')
    5
    '''
    atoms = 0
    i = 0
    while i < len(compost):
        if compost[i].isupper():
            if i + 1 < len(compost) and compost[i + 1].islower():
                i += 2
            else:
                i += 1
            atoms += 1
            if i < len(compost) and compost[i].isdigit():
                num_atoms = ''
                while i < len(compost) and compost[i].isdigit():
                    num_atoms += compost[i]
                    i += 1
                atoms += int(num_atoms) - 1
        else:
            i += 1
    return atoms

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)