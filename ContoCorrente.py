class ContoCorrente (nome, conto, saldo):
    def __init__ (nome, conto, importo):
        self.noime = nome
        self.conto = conto
        self.saldo = saldo

    def preleva (self, importo):
        self.saldo = saldo-importo

    def deposita (self, importo):
        self.saldo = saldo+importo

    def descrizione (self):
        print ('Il proprietario del conto è ' self.nome, 'Con il Conto '
               self.conto 'ed il Saldo è' self.saldo);
c1=ContoCorrente ("Francesco", "10", 17000)
c2=ContoCorrente ("Sara", "20", 29000)

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
