def mediana(lista_numeri):
    """
    torna il valore mediano, ovvero
    (elemento_centrale + elemento_precedente_a_quello_centrale) / 2
    """
    lista_numeri = sorted(lista_numeri)
    lung = len(lista_numeri)
    posizione_centrale = lung // 2
    elemento_centrale = lista_numeri[posizione_centrale] 
    posizione_precedente = posizione_centrale -1
    elemento_precedente = lista_numeri[posizione_precedente]
    return (elemento_centrale + elemento_precedente) // 2
    
if __name__ == '__main__':
    a = 0,1,2,67,12,456,798,54,32,2,34,545,776,8,0,6,3,343,465,78,87,6
    mediana(a)
