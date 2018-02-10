import random

def randomizza_lettere_parole_lista(lista):
    """
        ricordati di utilizzare le copie degli oggetti
        altrimenti il puntatore crea bug
        quando modifichi gli elementi di un oggetto mentre lo iteri
    """
    a = []
    for i in lista:
        parola = [e for e in i]
        random.shuffle(parola)
        print(parola)
        a.append(''.join(parola))
    return a

a = ['ciao', 'imola', 'ancora', 'orme']
randomizza_lettere_parole_lista(a)
