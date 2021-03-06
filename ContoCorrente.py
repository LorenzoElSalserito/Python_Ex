class Conto:
    def __init__ (nome, conto):
        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):
    def __init__ (self, importo):
        super().__init__(nome, conto)
        self._saldo = importo

    def preleva (self, importo):
        self.saldo -= importo

    def deposita (self, importo):
        self.saldo += importo

    def descrizione (self):
        print ('Il proprietario del conto è ' self.nome, 'Con il Conto '
               self.conto 'ed il Saldo è' self._saldo);

@property
    def saldo (self):
        print ("In questo momento sono dentro il getter")
        return self._saldo

@saldo.setter
    def saldo (self, importo)
    print ("In questo momento sono dentro il setter")
        self.preleva(self._saldo)
        self.deposita(importo)

class GestoreContiCorrenti:
    @staticmethod
    def bonifico(contosorgente, contodestinatario, trasferimento)
        contosorgente.preleva(trasferimento)
        contodestinatario.deposita(trasferimento)


c1 = ContoCorrente ("Antonio", "10", 50000)
c2 = ContoCorrente ("Sandra", "20", 90000)

c1.descrizione
c2.descrizione

GestoreContiCorrenti.bonifico(c1, c2, 1000)

c1.descrizione
c2.descrizione


c1.descrizione()
c2.descrizione()

c1.deposita(3500)
c2.deposita(5000)

c1.descrizione()
c2.descrizione()

c1.preleva(200)
c2.preleva(800)

c1.descrizione()
c2.descrizione()
