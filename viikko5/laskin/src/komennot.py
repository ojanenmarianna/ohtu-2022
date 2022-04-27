class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
    
    def suorita(self):
        luku = int(self._syote())
        return self._sovelluslogiikka.plus(luku)

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
    
    def suorita(self):
        luku = int(self._syote())
        return self._sovelluslogiikka.miinus(luku)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):

        return self._sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.kumoa()