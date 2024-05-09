#--------------- Inheritance  ------------------#
class Player:
    sinif = "Ag"
    sinif2 = "Qara"

    def __init__(self, sah, vezir, top, at, fil, piyada):
        self.sah = sah
        self.vezir = vezir
        self.top = top
        self.at = at
        self.fil = fil
        self.piyada = piyada


Oyuncu1 = Player(1, 1, 2, 2, 2, 8)
Oyuncu2 = Player(1, 1, 2, 2, 2, 8)


class Hucum:
    def __init__(self):
        pass

    def hucum_kec(self):
        print("Hucuma kecdi")

    def atak(self):
        print("Qarsi ataka basladi.")

    def mat(self):
        print("Sah ve mat oyun bitdi.")


class Mudafie(Hucum):
    def __init__(self):
        super().__init__()
        print("Oyun basladi.")

    def mudafie_et(self):
        print("Mudafie edir")

    def azalma(self):
        print("Mudafie etdikce zeifleyir.")


hucum = Hucum()
mudafie = Mudafie()
print(
    f"\nOyuncu {Oyuncu1.sinif} kvadratda oynayir. {Oyuncu1.sah} sah, {Oyuncu1.vezir} vezir, {Oyuncu1.top} top, {Oyuncu1.at} at, {Oyuncu1.fil} fil ve {Oyuncu1.piyada} piyada ile oyuna baslayir.\n"
)
print(
    f"Oyuncu {Oyuncu2.sinif2} kvadratda oynayir. {Oyuncu2.sah} sah, {Oyuncu2.vezir} vezir, {Oyuncu2.top} top, {Oyuncu2.at} at, {Oyuncu2.fil} fil ve {Oyuncu2.piyada} piyada ile oyuna baslayir.\n"
) 
print(f"\n{Oyuncu1.sinif} kvadratda oynayan oyuncu.")
hucum.hucum_kec()
print(f"\n{Oyuncu2.sinif2} kvadratda oynayan oyuncu.")
mudafie.mudafie_et()
mudafie.azalma()
print(f"\n{Oyuncu2.sinif2} kvadratda oynayan oyuncu.")
mudafie.atak()
print(f"\n{Oyuncu1.sinif} kvadratda oynayan oyuncu.")
hucum.hucum_kec()
hucum.mat()

#--------------- Polymorphism ------------------#

def chess(chess_win):
    chess_win.hucum_kec()
    chess_win.mudafie_et() 
    
# chess(hucum)
# chess(mudafie)