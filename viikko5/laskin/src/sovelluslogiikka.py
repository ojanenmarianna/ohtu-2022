class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.tulokset = []

    def miinus(self, arvo):
        self.tulokset.append(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulokset.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulokset.append(self.tulos)
        self.tulos = 0

    def kumoa(self):
        self.tulos = self.tulokset.pop(-1)

    def aseta_arvo(self, arvo):
        self.tulos = arvo