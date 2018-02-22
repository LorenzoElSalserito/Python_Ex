def crea_testo (stringa):
    """
        Con questa funzione posso aprire un file .txt
    """
    testo = open('/Scrivania/testo_di_prova.txt', 'w')
    
    
def scrivi (stringa):
	"""
	    Con questa funzione scrivo il benvenuto sul testo sopra indicato
	"""
	testo.write (input('Scrivi il testo che vuoi inserire: '))
	
	
def chiudi (stringa):
	testo.close


crea_testo (testo)
scrivi (testo)
chiudi (testo)
