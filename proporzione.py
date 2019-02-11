import string
"""
Questo programma prende in input numero, e, in base agli elementi considerati,
che possono essere le posizioni delle lettere di un set ASCII, ti da la posizione
della lettera corrispondente. Ovviamente nel caso delle lettere, andrebbe
implementato un programma che ti da il range delle lettere da usare al posto
di 'elementi', in questo programma
"""
def proporzione (numero, elementi):
    n_input = abs(numero)
    n_massimo = elementi
    while n_massimo <= n_input:
        n_input -= n_massimo
        if n_input <= n_massimo:
            return n_input
        if numero < 0:
            return -n_input

numero=25225246
elementi=100
proporzione(numero, elementi)
