#def fibonacci (n): #questa è la versione con il condizionale
    if n == 0 or n == 1:
        return 1;
    else:
        temp = fibonacci (n-1) + fibonacci (n-2);
        return temp;


def fibonacci (n): #stesso funzionamento, ma iterando con il while, posso elaborare numeri grandi in molto meno tempo
    a,b = 0, 1;
    while a < n:
        print (a, end=' ');
        a, b = b, a+b;
        print ()
