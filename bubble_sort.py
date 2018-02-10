def bubbleSort(alist):
    """
    sempre meglio creare una copia piuttosto che modificare valori per tramite di puntatori
    altrimenti nell'esecuzione del programma risulta difficile comprendere in quale momento e posizione
    all'interno del codice è avvenuta la sovrascrittura (eviti bug)
    """
    nlist = [a for a in alist]
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    print(alist, ' -> ', nlist)
    return nlist


alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
