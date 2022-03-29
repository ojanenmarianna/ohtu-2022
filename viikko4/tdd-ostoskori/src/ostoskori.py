from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.ostoskori:
            maara += ostos.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0.0
        for ostos in self.ostoskori:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        tuote = Ostos(lisattava)

        for ostos in self.ostoskori:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                return
        
        self.ostoskori.append(tuote)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        poistettava = Ostos(poistettava)
        for ostos in self.ostoskori:
            if poistettava.tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)


    def tyhjenna(self):
        self.ostoskori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
