from abc import ABC, abstractmethod
from datetime import date

# Absztrakt Auto osztály
class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass

# Szemelyauto osztaly
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasszam):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasszam = utasszam

    def __str__(self):
        return f"Szemelyauto | Rendszam: {self.rendszam}, Tipus: {self.tipus}, Utasszam: {self.utasszam}, Dij: {self.berleti_dij} Ft"

# Teherauto osztaly
class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherauto | Rendszam: {self.rendszam}, Tipus: {self.tipus}, Teherbiras: {self.teherbiras} kg, Dij: {self.berleti_dij} Ft"

# Berles osztaly
class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"Berles: {self.auto.rendszam} | Datum: {self.datum} | Ar: {self.auto.berleti_dij} Ft"

# Autokolcsonzo osztaly
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_hozzaadasa(self, auto):
        self.autok.append(auto)

    def auto_berlese(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                for berles in self.berlesek:
                    if berles.auto.rendszam == rendszam and berles.datum == datum:
                        print("Az auto ezen a napon mar foglalt.")
                        return
                uj_berles = Berles(auto, datum)
                self.berlesek.append(uj_berles)
                print(f"Sikeres berles: {uj_berles}")
                return
        print("Nem talalhato ilyen rendszamu auto.")

    def berles_lemondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                print(f"Berles lemondva: {berles}")
                return
        print("Ilyen berles nem talalhato.")

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincs aktiv berles.")
        for berles in self.berlesek:
            print(berles)

# Elokeszites
kolcsonzo = Autokolcsonzo("CityCar Kft.")

# Autok hozzaadasa
kolcsonzo.autok_hozzaadasa(Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5))
kolcsonzo.autok_hozzaadasa(Teherauto("XYZ-456", "Ford Transit", 15000, 1200))
kolcsonzo.autok_hozzaadasa(Szemelyauto("DEF-789", "Honda Civic", 11000, 5))

# Berlesek hozzaadasa
kolcsonzo.auto_berlese("ABC-123", date(2025, 4, 13))
kolcsonzo.auto_berlese("XYZ-456", date(2025, 4, 13))
kolcsonzo.auto_berlese("DEF-789", date(2025, 4, 14))
kolcsonzo.auto_berlese("ABC-123", date(2025, 4, 15))

# Egyszeru CLI felulet
while True:
    print("\n--- Autokolcsonzo Menu ---")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("0. Kilépés")

    valasztas = input("Válassz egy lehetőséget: ")

    if valasztas == "1":
        rendszam = input("Add meg az autó rendszámát: ")
        ev = int(input("Év: "))
        honap = int(input("Hónap: "))
        nap = int(input("Nap: "))
        kolcsonzo.auto_berlese(rendszam, date(ev, honap, nap))
    elif valasztas == "2":
        rendszam = input("Add meg a rendszámot a lemondáshoz: ")
        ev = int(input("Év: "))
        honap = int(input("Hónap: "))
        nap = int(input("Nap: "))
        kolcsonzo.berles_lemondasa(rendszam, date(ev, honap, nap))
    elif valasztas == "3":
        kolcsonzo.berlesek_listazasa()
    elif valasztas == "0":
        print("Kilépés... Viszlát!")
        break
    else:
        print("Érvénytelen választás!")
