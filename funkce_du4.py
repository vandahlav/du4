import json
from json.decoder import JSONDecodeError

#funkce pro načtení souboru
def otevreni_souboru(soubor):
    try:
        data = {}
        with open(soubor, "r",  encoding="utf-8") as in_file:
            data = json.load(in_file)
            return data
    except FileNotFoundError:
        print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
        quit()
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()
    except JSONDecodeError:
        print("Načtený vstupní soubor není platný JSON.")
        quit()
    except FileNotFoundError:
        print("Program nemá povolen přístup k datům.")
        quit()

#funkce zápis do výstupního souboru
def pristup_k_souboru(output_soubor):
    try: 
        with open(output_soubor, "w", encoding="utf-8") as zapis:     
            json.dump(output_soubor, zapis)
    except PermissionError:
        print("Program nemá přístup k zápisu výstupních souborů.")
        quit()

"""
#pomohla by class? nějak?
class Writer():
    def __init__(self, data):
        self.data = data
        self.nove_souradnice = []
    
    def output (self):
        try: 
            with open(self.data, "w", encoding="utf-8") as zapis: 
                zapisuju_sem = []    
                for line in self.nove_souradnice:
                    zapisuju_sem.append(line.zapis())               
                json.dump(self.data, zapis)
        except PermissionError:
            print("Program nemá přístup k zápisu výstupních souborů.")
            quit()"""

#funkce pro kontrolu maximální délky
def je_cislo(n):
    try:
        cislo = int(n)
    except ValueError:
        print("Chybně zadána maximální délka segmentu. Program končí.")
        quit()
    if cislo < 0:
        print("Bylo zadáno záporné číslo, program skončí.")
        quit()