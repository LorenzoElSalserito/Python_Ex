import shutil
import os


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


def leggi (stringa):
	documento=testo.read ()
	print (documento)


def copia (stringa):
	shutil.copy(input('scrivi la destinazione finale della copia del testo '))


def muovi (stringa):
	shutil.move(input('scrivi la destinazione finale del testo '))


def rinomina (stringa):
	os.rename(input('inserisci il file da rinominare: '),
	          input('inserisci il nuovo nome del file: '))


def cancella (stringa):
	os.unlink(input('scrivi il percorso del file da eliminare: '))


crea_testo (testo)
scrivi (testo)
leggi (testo)
chiudi (testo)
copia (testo)
muovi (testo)
rinomina (testo)
cancella (testo)
