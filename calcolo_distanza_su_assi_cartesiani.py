def distanza (x1, x2, y1, y2):
    dx = x2 - x1;
    dy = y2 - y1;
    quadrati = dx**2 + dy**2;
    risultato = math.sqrt(quadrati);
    return risultato;
