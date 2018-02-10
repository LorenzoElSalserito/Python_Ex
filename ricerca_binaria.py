def ricerca_binaria(lista, valore_cercato):
    """
    NON PROPRIO come illustrato nel libro di Libero Nigro

    cerca il valore_cercato tra un valore inferiore e un valore superiore
    se esiste nella lista, altrimenti torna Eccezione (==FALSO)
    """
    if valore_cercato not in lista:
        raise Exception("valore_cercato non esiste nella lista")

    lista.sort()
    lista = list(set(lista))
    if valore_cercato == lista[0] or valore_cercato == lista[-1]:
        raise Exception("il valore_cercato è troppo estremo "
                        "all'interno della lista."
                        "Prova ad immettere un altro valore")
    
    posizione_valore_cercato = lista.index(valore_cercato)
    inferiore = lista[posizione_valore_cercato-1]
    superiore = lista[posizione_valore_cercato+1]
    print(inferiore, valore_cercato, superiore)
    return True

a = [1, 1, 2, 3, 3, 4, 6, 7, 7, 7, 9]
ricerca_binaria(a, 4)
