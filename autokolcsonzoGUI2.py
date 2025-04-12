import tkinter as tk
from tkinter import messagebox
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

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utasszam):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utasszam = utasszam

    def __str__(self):
        return f"Személyautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Utasszám: {self.utasszam}, Díj: {self.berleti_dij} Ft"

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras} kg, Díj: {self.berleti_dij} Ft"

class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"Bérlés: {self.auto.rendszam} | Dátum: {self.datum} | Ár: {self.auto.berleti_dij} Ft"

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
                        return "Az autó ezen a napon már foglalt."
                uj_berles = Berles(auto, datum)
                self.berlesek.append(uj_berles)
                return f"Sikeres bérlés: {uj_berles}"
        return "Nem található ilyen rendszámú autó."

    def berles_lemondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                return f"Bérlés lemondva: {berles}"
        return "Ilyen bérlés nem található."

    def berlesek_listazasa(self):
        return [str(berles) for berles in self.berlesek] if self.berlesek else ["Nincs aktív bérlés."]

# Példányosítás
kolcsonzo = Autokolcsonzo("CityNero Kft.")
kolcsonzo.autok_hozzaadasa(Szemelyauto("RYM-123", "Skoda Kodiaq", 10000, 5))
kolcsonzo.autok_hozzaadasa(Teherauto("XXZ-456", "Renault Boxer", 15000, 1200))
kolcsonzo.autok_hozzaadasa(Szemelyauto("DEE-789", "Opel Astra", 11000, 5))
kolcsonzo.auto_berlese("RYM-123", date(2025, 4, 13))
kolcsonzo.auto_berlese("XXZ-456", date(2025, 4, 13))
kolcsonzo.auto_berlese("DEE-789", date(2025, 4, 14))
kolcsonzo.auto_berlese("RYM-123", date(2025, 4, 15))

# Grafikus felület
class AutoKolcsonzoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Autókölcsönző")

        tk.Label(master, text="Rendszám:").grid(row=0, column=0)
        self.rendszam_entry = tk.Entry(master)
        self.rendszam_entry.grid(row=0, column=1)

        tk.Label(master, text="Év:").grid(row=1, column=0)
        self.ev_entry = tk.Entry(master)
        self.ev_entry.grid(row=1, column=1)

        tk.Label(master, text="Hónap:").grid(row=2, column=0)
        self.honap_entry = tk.Entry(master)
        self.honap_entry.grid(row=2, column=1)

        tk.Label(master, text="Nap:").grid(row=3, column=0)
        self.nap_entry = tk.Entry(master)
        self.nap_entry.grid(row=3, column=1)

        tk.Button(master, text="Autó bérlése", command=self.berles).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Bérlés lemondása", command=self.lemondas).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Bérlések listázása", command=self.listazas).grid(row=6, column=0, columnspan=2, pady=5)

    def get_datum(self):
        try:
            ev = int(self.ev_entry.get())
            honap = int(self.honap_entry.get())
            nap = int(self.nap_entry.get())
            return date(ev, honap, nap)
        except ValueError:
            messagebox.showerror("Hiba", "Érvénytelen dátum!")
            return None

    def berles(self):
        rendszam = self.rendszam_entry.get()
        datum = self.get_datum()
        if datum:
            uzenet = kolcsonzo.auto_berlese(rendszam, datum)
            messagebox.showinfo("Bérlés", uzenet)

    def lemondas(self):
        rendszam = self.rendszam_entry.get()
        datum = self.get_datum()
        if datum:
            uzenet = kolcsonzo.berles_lemondasa(rendszam, datum)
            messagebox.showinfo("Lemondás", uzenet)

    def listazas(self):
        berlesek = kolcsonzo.berlesek_listazasa()
        messagebox.showinfo("Aktív bérlések", "\n".join(berlesek))

# GUI indítása
root = tk.Tk()
app = AutoKolcsonzoGUI(root)
root.mainloop()