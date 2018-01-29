def contatore_multi(elemento_iterabile):
    """
    contatore_multi('cacca')
    #returns: {'c': 3, 'a': 2}
    """
    d = {}
    for ele in elemento_iterabile:
        if d.get(ele): d[ele] += 1
        else: d[ele] = 1
    return d
