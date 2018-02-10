def stampa_stringa_come(stringa, formato='int'):
    """
      formato = 'int', 'hex', 'bin'
    """
    for i in stringa:
        n = ord(i)
        if formato == 'hex':
            print(hex(n))
        elif formato == 'bin':
            print(bin(n))
        else:
            print(n)
